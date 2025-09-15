"""
Inspect types and the attributes and properties of
Todo and Workspace objects for querying
"""

from inspect import getmembers, get_annotations, signature, Signature
from typing import ForwardRef, get_args

from dooit.api import Todo, Workspace
from sqlalchemy.orm.util import GenericAlias


def has_forward_ref(value_type: type) -> bool:
    args = get_args(value_type)
    for arg in args:
        if isinstance(arg, ForwardRef):
            return True
    return False


def to_bool(value) -> bool:
    if isinstance(value, bool):
        return value

    if value.lower() in ("true", "t", "yes", "y", "1"):
        return True

    if value.lower() in ("false", "f", "no", "n", "0"):
        return False

    raise ValueError("invalid literal for boolean: %s" % value)


class OptionInspector:
    attr: dict[str, type] = dict()
    prop: dict[str, type] = dict()

    # Only stores values can work as user inputs
    input_attr: dict[str, type] = dict()
    input_prop: dict[str, type] = dict()

    def __init__(self, query_class):
        annotations = get_annotations(query_class)

        # Store public properties & attributes
        for name, value in getmembers(query_class):
            if callable(value) or name.startswith("_"):
                continue

            if isinstance(value, property):
                return_type = signature(value.fget).return_annotation
                self.prop[name] = return_type

                # TODO: allow list query inputs
                if return_type != Signature.empty and not has_forward_ref(return_type):
                    self.input_prop[name] = return_type
            elif name in annotations:
                attr_type = annotations[name]
                if isinstance(attr_type, GenericAlias):
                    attr_type = get_args(attr_type)[0]

                self.attr[name] = attr_type
                if not has_forward_ref(attr_type):
                    self.input_attr[name] = attr_type

    def get_type(self, name: str) -> type:
        if name in self.attr:
            return self.attr[name]

        if name in self.prop:
            return self.prop[name]

        raise AttributeError("invalid attribute or property name: '%s'" % name)

    def get_type_str(self, name: str) -> str:
        type_obj = self.get_type(name)

        if len(get_args(type_obj)) == 0:
            return type_obj.__name__

        return repr(type_obj).removeprefix(type_obj.__module__ + ".")


todo_opts = OptionInspector(Todo)
workspace_opts = OptionInspector(Workspace)
