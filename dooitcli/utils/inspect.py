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
        # HACK: this is iffy
        self.input_attr = {
            k: v
            for k, v in self.attr.items()
            if not isinstance(recurse_type(v), ForwardRef)
        }

        self.input_prop: dict[str, property] = dict()
        for k, v in self.prop.items():
            if k not in ("has_same_parent_kind", "session"):
                try:
                    if return_sig_type(v).__name__ not in ("List", "Union"):
                        self.input_prop[k] = v
                except AssertionError:
                    self.input_prop[k] = v

        self.input_options = self.input_attr | self.input_prop

    def attr_type(self, name: str) -> type:
        return recurse_type(self.attr[name])

    def attr_type_str(self, name: str) -> str:
        return self.attr_type(name).__name__

    def prop_type(self, name: str) -> type:
        return return_sig_type(self.prop[name])

    def prop_type_str(self, name: str) -> str:
        return self.prop_type(name).__name__


todo_opts = InspectOptions(Todo)
workspace_opts = InspectOptions(Workspace)
