"""
Functions to traverse dooit's Workspace and Todo trees
"""

from dooit.api import Todo


def _recurse_todo_tail(todo: Todo, lst: list[Todo]) -> None:
    lst.append(todo)
    for child in todo.todos:
        _recurse_todo_tail(child, lst)


def recurse_todo(todo: Todo) -> list[Todo]:
    """
    Given a Todo object, checks if it has subtodos.
    If so, this function recurses for each subtodo.

    Returns a list with the input Todo and all descendant Todo objects.
    """

    result = [todo]

    for child in todo.todos:
        _recurse_todo_tail(child, result)

    return result


def _get_ancestors_tail(todo: Todo, lst: list[Todo]) -> None:
    if not todo.parent_todo:
        return
    lst.append(todo.parent_todo)
    _get_ancestors_tail(todo.parent_todo, lst)


def get_ancestors(todo: Todo) -> list[Todo]:
    """
    Returns all parents, grandparents, etc. of the input Todo.
    """

    result = []
    _get_ancestors_tail(todo, result)
    return result
