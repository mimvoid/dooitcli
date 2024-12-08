from dooit.api import Workspace, Todo
import click

from ...utils.todo import recurse_todo, due_string
from . import format


@click.pass_context
def todo_to_markdown(ctx, todo: Todo) -> list[str]:
    """
    Takes in a dooit Todo object and fetches any existing subtodos.
    Returns a list of the todo/s as strings in Markdown format.
    """

    todos = recurse_todo(todo)

    lines = []

    for i in todos:
        indent = " " * (i.nest_level * 4)
        checkbox = format.checkbox(i.status)

        text = indent + checkbox + i.description

        if ctx.obj["DUE"]:
            if ctx.obj["DATAVIEW"]:
                text += format.dataview_due(i.due)
            else:
                text += due_string(i.due)

        if ctx.obj["URGENCY"]:
            text += format.urgency(i.urgency)

        if ctx.obj["EFFORT"]:
            text += format.effort(i.effort)

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

    # Exclude workspaces with no todos
    if len(current.todos) == 0:
        return []

    # Format the heading with padding
    heading = format.heading(current.nest_level, current.description)
    if first:
        lines = [heading, ""]
    else:
        lines = ["", heading, ""]

    # Format the todos
    for i in current.todos:
        lines += todo_to_markdown(i)

    return lines + dooit_to_markdown(workspaces, index + 1, first=False)
