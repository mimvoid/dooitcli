"""
Inspect types and the attributes and properties of
Todo and Workspace objects for querying
"""

from inspect import getmembers, ismethod, get_annotations, signature, Signature
from typing import Any, ForwardRef

from dooit.api import Todo, Workspace


def return_sig_type(value: property) -> type:
    value_type = signature(value.fget).return_annotation

    assert value_type != Signature.empty
    return value_type


def recurse_type(value_type: type) -> type:
    if not hasattr(value_type, "__args__"):
        return value_type

    return recurse_type(value_type.__args__[0])


def to_bool(value) -> bool:
    if isinstance(value, bool):
        return value

    if value.lower() in ("true", "t", "yes", "y", "1"):
        return True

    if value.lower() in ("false", "f", "no", "n", "0"):
        return False

    raise ValueError("invalid literal for boolean: %s" % value)


class InspectOptions:
    def __init__(self, query_class):
        self.attr: dict[str, Any] = dict()
        self.prop: dict[str, property] = dict()

        annotations = get_annotations(query_class)

        # Store public properties & attributes
        for name, value in getmembers(
            query_class, lambda v: not ismethod(v) and not callable(v)
        ):
            if not name.startswith("_"):
                if isinstance(value, property):
                    self.prop[name] = value
                elif name in annotations:
                    self.attr[name] = annotations[name]

        self.options = self.attr | self.prop

        # Filter out values that can't work as user inputs
        self.input_attr = {
            k: v
            for k, v in self.attr.items()
            if not isinstance(recurse_type(v), ForwardRef)
        }

        self.input_prop: dict[str, property] = dict()
        for k, v in self.prop.items():
            if k not in ("has_same_parent_kind", "session"):
                try:
                    if not issubclass(return_sig_type(v), list):
                        self.input_prop[k] = v
                except AssertionError:
                    self.input_prop[k] = v
                except TypeError:
                    pass

        self.input_options = self.input_attr | self.input_prop

    def get_type(self, name: str) -> type:
        if name in self.attr:
            return recurse_type(self.attr[name])

        if name in self.prop:
            return return_sig_type(self.prop[name])

        raise AttributeError("invalid attribute or property name: '%s'" % name)

    def get_type_str(self, name: str) -> str:
        return self.get_type(name).__name__


todo_opts = InspectOptions(Todo)
workspace_opts = InspectOptions(Workspace)
