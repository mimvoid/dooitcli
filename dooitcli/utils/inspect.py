"""
Inspect types and the attributes and properties of
Todo and Workspace objects for querying
"""

from inspect import getmembers, ismethod, get_annotations, signature, Signature
from typing import Any, ForwardRef

from dooit.api import Todo, Workspace


def return_sig_type(value: property) -> type:
    return signature(value.fget).return_annotation


def recurse_type(value_type: type) -> type:
    if hasattr(value_type, "__args__"):
        return recurse_type(value_type.__args__[0])

    return value_type


def to_bool(value) -> bool:
    if isinstance(value, bool):
        return value

    if value.lower() in ("true", "t", "yes", "y", "1"):
        return True

    if value.lower() in ("false", "f", "no", "n", "0"):
        return False

    raise ValueError("invalid literal for boolean: %s" % value)


class OptionInspector:
    attr: dict[str, Any] = dict()
    prop: dict[str, property] = dict()

    # Only stores values can work as user inputs
    input_attr: dict[str, Any] = dict()
    input_prop: dict[str, property] = dict()

    def __init__(self, query_class):
        annotations = get_annotations(query_class)

        # Store public properties & attributes
        for name, value in getmembers(query_class):
            if ismethod(value) or callable(value) or name.startswith("_"):
                continue

            if isinstance(value, property):
                self._add_property(name, value)
            elif name in annotations:
                self.attr[name] = annotations[name]
                if not isinstance(recurse_type(value), ForwardRef):
                    self.input_attr[name] = annotations[name]

    def _add_property(self, name: str, value: property) -> None:
        if name in ("has_same_parent_kind", "session"):
            return

        self.prop[name] = value

        try:
            # TODO: allow list query inputs
            if value != Signature.empty and not issubclass(
                return_sig_type(value), list
            ):
                self.input_prop[name] = value
        except TypeError:
            return

    def get_type(self, name: str) -> type:
        if name in self.attr:
            return recurse_type(self.attr[name])

        if name in self.prop:
            return return_sig_type(self.prop[name])

        raise AttributeError("invalid attribute or property name: '%s'" % name)

    def get_type_str(self, name: str) -> str:
        return self.get_type(name).__name__


todo_opts = OptionInspector(Todo)
workspace_opts = OptionInspector(Workspace)
