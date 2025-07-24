"""
Functions to traverse dooit's Workspace and Todo trees
"""

from dooit.api import Todo


def recurse_todo(todo: Todo) -> list[Todo]:
    """
    Given a Todo object, checks if it has subtodos.
    If so, this function recurses for each subtodo.

    Returns a list with the input Todo and all descendant Todo objects.
    """

    result = [todo]

    for child in todo.todos:
        result += recurse_todo(child)

    return result


def get_ancestors(todo: Todo) -> list[Todo]:
    """
    Returns all parents, grandparents, etc. of the input Todo.
    """

    if not todo.parent_todo:
        return []

    return [todo.parent_todo] + get_ancestors(todo.parent_todo)
