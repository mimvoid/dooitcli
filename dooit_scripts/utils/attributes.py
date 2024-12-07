from inspect import getmembers, ismethod, signature, Signature
from typing import Callable


def get_attrs(object) -> set[str]:
    """
    Finds all attributes and properties of an Object.
    Excludes methods and functions.
    """

    attrs = set()

    for name, value in getmembers(object):
        if (not name.startswith("_")) and (not ismethod(value)):
            attrs.add(name)

    return attrs


def get_property_return_type(func: Callable):
    sig = signature(func)
    return_type = sig.return_annotation

    if return_type == Signature.empty:
        return

    return return_type
