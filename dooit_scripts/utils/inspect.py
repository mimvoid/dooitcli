from inspect import getmembers, ismethod, signature, Signature
from typing import Callable


def get_attrs(object) -> set[str]:
    """
    Finds all attributes of an Object or Class.
    Excludes methods and functions.
    """

    attrs = set()

    for name, value in getmembers(object):
        if (not name.startswith("_")) and (not ismethod(value)) and (not callable(value)):
            attrs.add(name)

    return attrs


def get_props(object) -> set[str]:
    """
    Finds functions of an Object or Class.
    """

    props = set()

    for name, value in getmembers(object):
        if (not name.startswith("_")) and (not ismethod(value)) and (callable(value)):
            props.add(name)

    return props


def get_return_type(func: Callable):
    """
    Fetches a function's signature and finds its return type annotation.
    Returns an AssertionError if the annotation is empty.
    """

    sig = signature(func)
    return_type = sig.return_annotation

    assert return_type != Signature.empty
    return return_type
