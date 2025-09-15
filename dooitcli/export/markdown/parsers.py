from argparse import Namespace

from dooit.api import Workspace, Todo

from ...utils.format import due_str
from ...utils.tree import recurse_todo
from . import format


def todo_to_markdown(args: Namespace, todo: Todo) -> str:
    indent = " " * (todo.nest_level * 4)
    checkbox = format.checkbox(todo.status, args.nonstandard)

    text = [indent, checkbox, todo.description]

    if args.due:
        if args.dataview:
            text.append(format.dataview_due(todo.due, args.date))
        elif todo.due is not None:
            text.append(f"  (due: {due_str(todo.due, args.date, args.time)})")

    if args.urgency:
        text.append(format.urgency(todo.urgency, args.dataview))
    if args.effort:
        text.append(format.effort(todo.effort, args.dataview))

    return "".join(text)


def todo_tree_to_markdown(args: Namespace, todo: Todo) -> list[str]:
    """
    Takes in a dooit Todo object and fetches any existing subtodos.
    Returns a list of the todo/s as strings in Markdown format.
    """

    return [todo_to_markdown(args, i) for i in recurse_todo(todo)]


def workspace_to_markdown(
    args: Namespace, workspace: Workspace, index: int
) -> list[str]:
    # Format the heading with padding
    heading = format.heading(workspace.nest_level, workspace.description)
    lines = [heading, ""] if index == 0 else ["", heading, ""]

    # Format the todos
    for i in workspace.todos:
        lines += todo_tree_to_markdown(args, i)

    return lines


def dooit_to_markdown(args: Namespace, workspaces: list[Workspace]) -> list[str]:
    """
    Iterates over a list of dooit Workspace objects.

    Returns a list of Markdown formatted lines with headings and task lists
    for each Workspace.
    """

    result = []
    for i, ws in enumerate(workspaces):
        if not ws.todos:
            continue  # Skip workspaces with no todos
        result += workspace_to_markdown(args, ws, i)

    return result
