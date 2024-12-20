from dooit.api import Workspace, Todo

from ...utils.todo import recurse_todo, due_string
from . import format


def todo_to_markdown(args, todo: Todo) -> list[str]:
    """
    Takes in a dooit Todo object and fetches any existing subtodos.
    Returns a list of the todo/s as strings in Markdown format.
    """

    todos = recurse_todo(todo)

    lines = []

    for i in todos:
        indent = " " * (i.nest_level * 4)
        checkbox = format.checkbox(args, i.status)

        text = indent + checkbox + i.description

        if args.due:
            if args.dataview:
                text += format.dataview_due(args, i.due)
            elif i.due is not None:
                text += f"  (due: {due_string(args, i.due)})"

        if args.urgency:
            text += format.urgency(args, i.urgency)

        if args.effort:
            text += format.effort(args, i.effort)

        lines.append(text)

    return lines


def dooit_to_markdown(
    args, workspaces: list[Workspace], index: int = 0, first: bool = True
) -> list[str]:
    """
    Iterates over a list of dooit Workspace objects.

    Returns a list of Markdown formatted lines with headings and task lists
    for each Workspace.
    """

    if index >= len(workspaces):
        return []

    current = workspaces[index]

    # Exclude workspaces with no todos
    if current.todos == []:
        return []

    # Format the heading with padding
    heading = format.heading(current.nest_level, current.description)
    if first:
        lines = [heading, ""]
    else:
        lines = ["", heading, ""]

    # Format the todos
    for i in current.todos:
        lines += todo_to_markdown(args, i)

    return lines + dooit_to_markdown(args, workspaces, index + 1, first=False)
