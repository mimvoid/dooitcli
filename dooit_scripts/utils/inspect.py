from inspect import getmembers, ismethod, signature, Signature
from typing import Any

from dooit.api import Todo, Workspace


class InspectOptions:
    def __init__(self, query_class):
        self.attributes: dict[str, Any] = dict()
        self.properties: dict[str, property] = dict()

        for name, value in getmembers(query_class):
            if (
                (not name.startswith("_"))
                and (not ismethod(value))
                and (not callable(value))
            ):
                if isinstance(value, property):
                    self.properties[name] = value
                else:
                    self.attributes[name] = value

        self.options = self.attributes | self.properties

    def return_type(self, name: str) -> type | None:
        if name in self.attributes:
            # FIX
            return type(self.attributes[name])
        elif name in self.properties:
            prop = self.properties[name]
            value_return_type = signature(prop.fget).return_annotation

            assert value_return_type != Signature.empty
            return value_return_type

todo_opts = InspectOptions(Todo)
workspace_opts = InspectOptions(Workspace)
