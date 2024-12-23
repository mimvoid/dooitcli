from typing import Sequence

from dooit.api import Todo
from rich.table import Table
from rich.text import Text
from rich import box

from ..._rich import console
from ...utils.format import due_str
from ...utils.tree import get_ancestors


def icon_status(status: str) -> Text:
    match status:
        case "completed":
            return Text("x", style="green")
        case "pending":
            return Text("o", style="yellow")
        case "overdue":
            return Text("!", style="red")
        case _:
            return Text("")


def color_urgency(urgency: int) -> Text:
    match urgency:
        case 4:
            color = "red"
        case 3:
            color = "yellow"
        case 2:
            color = "green"
        case _:
            color = "cyan"

    return Text(str(urgency), style=color)


def print_pretty_todos(args, todos: Sequence[Todo]) -> None:
    table = Table(
        box=box.ROUNDED,
        border_style="yellow",
        show_header=(not args.no_header),
    )

    if args.id:
        table.add_column("ID", justify="right", style="white")

    # Status
    table.add_column("", justify="center")
    # Description
    table.add_column("Todo", justify="left")
    # Workspace
    table.add_column("Workspace", justify="left")

    if args.due:
        table.add_column("Due")
    if args.urgency:
        table.add_column("Urgency", justify="center")
    if args.effort:
        table.add_column("Effort", justify="center")

    for i in todos:
        row = []

        if args.id:
            row.append(str(i.id))

        row.append(icon_status(i.status))
        row.append(i.description)

        if not i.parent_workspace:
            row.append(
                Text(get_ancestors(i)[-1].parent_workspace.description, style="blue")
            )
        else:
            row.append(Text(i.parent_workspace.description, style="magenta"))

        if args.due:
            row.append(due_str(args, i.due))

        if args.urgency:
            row.append(color_urgency(i.urgency))

        if args.effort:
            row.append(str(i.effort))

        table.add_row(*row)

    console.print(table, new_line_start=True)


def print_plain_todos(args, todos: Sequence[Todo]) -> None:
    for i in todos:
        row = []

        if args.id:
            row.append(str(i.id))

        row.append(icon_status(i.status))
        row.append(i.description)

        if args.due:
            row.append(due_string(args, i.due))
        if args.urgency:
            row.append(i.urgency)
        if args.effort:
            row.append(str(i.effort))

        print(*row)
