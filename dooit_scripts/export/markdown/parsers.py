from dooit.api import Workspace, Todo

from ...utils.todo import recurse_todo
from . import formats as fmt


def todo_to_markdown(todo: Todo) -> list[str]:
    """
    Takes in a dooit Todo object and fetches any existing subtodos.
    Returns a list of the todo/s as strings in Markdown format.
    """

    todos = recurse_todo(todo)

    lines = []

    for i in todos:
        indent = " " * (i.nest_level * 4)
        checkbox = fmt.checkbox(i.status)

        text = indent + checkbox + i.description

        # if show_due:
        due_date = fmt.due_date(i.due)
        text += due_date

        lines.append(text)

    return lines


def dooit_to_markdown(
    workspaces: list[Workspace], index: int = 0, first: bool = True
) -> list[str]:
    """
    Iterates over a list of dooit Workspace objects.

    Returns a list of Markdown formatted lines with headings and task lists
    for each Workspace.
    """

    if index >= len(workspaces):
        return []

    current = workspaces[index]

    lines = []

    # Only get workspaces with todos
    if len(current.todos) > 0:
        heading = fmt.heading(current.nest_level, current.description)

        # Don't add an empty line before the first heading
        if first:
            lines = [heading, ""]
        else:
            lines = ["", heading, ""]

        for i in current.todos:
            lines += todo_to_markdown(i)

    return lines + dooit_to_markdown(workspaces, index + 1, first=False)
