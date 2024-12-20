from inspect import getmembers, ismethod, signature, Signature
from typing import Any

from dooit.api import Todo, Workspace


def return_sig_type(value: property) -> type | None:
    value_type = signature(value.fget).return_annotation

    assert value_type != Signature.empty
    return value_type


class InspectOptions:
    def __init__(self, query_class):
        self.attributes: dict[str, Any] = dict()
        properties: dict[str, property] = dict()

        # Store properties & attributes
        for name, value in getmembers(query_class):
            if (
                (not name.startswith("_"))
                and (not ismethod(value))
                and (not callable(value))
            ):
                if isinstance(value, property):
                    properties[name] = value
                else:
                    self.attributes[name] = value

        # Filter out values that can't work as user inputs
        self.properties: dict[str, property] = dict()
        for k, v in properties.items():
            try:
                # HACK: this is a little iffy
                if return_sig_type(v).__name__ not in ["List", "Union"]:
                    self.properties[k] = v
            except AssertionError:
                self.properties[k] = v

        self.options = self.attributes | self.properties

    def return_type(self, name: str) -> type | None:
        if name in self.attributes:
            # FIX
            return type(self.attributes[name])
        elif name in self.properties:
            return return_sig_type(self.properties[name])


todo_opts = InspectOptions(Todo)
workspace_opts = InspectOptions(Workspace)
