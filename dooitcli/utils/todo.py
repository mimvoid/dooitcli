import datetime
from typing import Sequence

from dooit.api import Todo, manager
from sqlalchemy import select

from .inspect import todo_opts

"""
Helper functions related to dooit's Todo object
"""


def due_string(args, date: datetime.datetime | None) -> str:
    if not date:
        return ""

    dt_format = args.date

    if date.hour != 0 or date.minute != 0:
        dt_format += args.time

    due = date.strftime(dt_format)
    return due


def filter_todo_db(attr, value) -> Sequence[Todo]:
    todo_attr = getattr(Todo, attr)
    query = select(Todo).where(todo_attr == value)
    res = manager.session.execute(query).scalars().all()
    return res


def filter_todos(todos: list[Todo], attr: str, value) -> Sequence[Todo]:
    """
    Takes in a list of Todo objects, a Todo attribute/property,
    and the value it should be.

    Returns a list of the Todo objects that match the attribute value.

    The matching is case insensitive.
    """

    if attr in todo_opts.attributes:
        return filter_todo_db(attr, value)

    result = []

    for todo in todos:
        todo_value = getattr(todo, attr)
        if todo_value == value:
            result.append(todo)

    return result


def recurse_todo(todo: Todo) -> list[Todo]:
    """
    Given a Todo object, checks if it has subtodos.
    If so, this function recurses for each subtodo.

    Returns a list with the input Todo and all descendant Todo objects.
    """

    result = [todo]

    if len(todo.todos) > 0:
        for child in todo.todos:
            result += recurse_todo(child)

    return result


def get_ancestors(todo: Todo) -> list[Todo]:
    """
    Returns all parents, grandparents, etc. of the input Todo.
    """

    if not todo.parent_todo:
        return []

    parent = todo.parent_todo

    return [parent] + get_ancestors(todo.parent_todo)
