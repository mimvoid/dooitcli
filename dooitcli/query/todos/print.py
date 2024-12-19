from typing import Sequence

from dooit.api import Todo
from rich.table import Table
from rich.text import Text
from rich import box

# from ...args.main import args
from ..._rich import console
from ...utils.todo import due_string


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
    table.add_column("Description", justify="left")

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

        if args.due:
            row.append(due_string(args, i.due))

        if args.urgency:
            row.append(str(i.urgency))

        if args.effort:
            row.append(str(i.effort))

        table.add_row(*row)

    console.print(table, new_line_start=True)


def print_plain_todos(todos: Sequence[Todo]) -> None:
    for i in todos:
        id, status, desc = str(i.id), icon_status(i.status), i.description
        print(id, status, desc)
