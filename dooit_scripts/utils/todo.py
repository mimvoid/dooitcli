import datetime

from dooit.api import Todo, manager
from sqlalchemy import select
import click

"""
Helper functions related to dooit's Todo object
"""


@click.pass_context
def due_string(ctx, date: datetime.datetime | None) -> str:
    if not date:
        return ""

    dt_format = ctx.obj["DATE"]

    if date.hour != 0 or date.minute != 0:
        dt_format += ctx.obj["TIME"]

    due = date.strftime(dt_format)
    return due


def sql_filter(attr, value) -> list[Todo]:
    query = select(Todo).where(attr == value)
    res = manager.session.execute(query).scalars().all()
    assert res is not None
    return res


def filter_todos(todos: list[Todo], attr: str, value) -> list[Todo]:
    """
    Takes in a list of Todo objects, a Todo attribute/property,
    and the value it should be.

    Returns a list of the Todo objects that match the attribute value.

    The matching is case insensitive.
    """

    result = []

    # Sanitized string
    fmt_value = str(value).strip().lower()

    for todo in todos:
        todo_value = getattr(todo, attr)
        fmt_todo_value = str(todo_value).strip().lower()

        if fmt_todo_value == fmt_value:
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
