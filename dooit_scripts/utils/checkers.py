import inspect


def get_attrs(object) -> list[str]:
    """
    Finds all attributes and properties of the Todo object
    and their values.

    Excludes methods and functions.
    """

    attrs = []

    for i in inspect.getmembers(object):
        name, value = i

        is_private = name.startswith("_")
        is_method = inspect.ismethod(value)

        if (not is_private) and (not is_method):
            attrs.append(i)

    return attrs


def is_valid_attr(object, attr: str) -> bool:
    valid_names = [i[0] for i in get_attrs(object)]
    return attr in valid_names
