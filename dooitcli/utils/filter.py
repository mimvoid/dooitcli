from typing import Any
from collections.abc import Sequence

from dooit.api import Todo, manager
from sqlalchemy import select

from .inspect import todo_opts


def filter_db(cls: type, attr: str, value: Any) -> Sequence:
    """
    Filters an object class with sqlalchemy
    """

    cls_attr = getattr(cls, attr)
    query = select(cls).where(cls_attr == value)

    return manager.session.execute(query).scalars().all()


def filter_obj(lst: Sequence, attr: str, value: Any) -> list:
    return list(filter(lambda obj: getattr(obj, attr) == value, lst))


def filter_todos(todos: Sequence[Todo], attr: str, value: Any) -> Sequence[Todo]:
    """
    Takes in a sequence of Todo objects, an attribute or property,
    and the value it should be.

    Returns a sequence of Todo objects that match the value.
    """

    if attr in todo_opts.attr:
        return filter_db(Todo, attr, value)

    return filter_obj(todos, attr, value)
