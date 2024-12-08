from typing import Sequence

from dooit.api import Todo
from rich.table import Table
from rich.text import Text
from rich import box
import click

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


@click.pass_context
def print_pretty_todos(ctx, todos: Sequence[Todo]) -> None:
    table = Table(
        box=box.ROUNDED,
        border_style="yellow",
        show_header=ctx.obj["HEADER"],
    )

    if ctx.obj["ID"]:
        table.add_column("ID", justify="right", style="white")

    # Status
    table.add_column("", justify="center")
    # Description
    table.add_column("Description", justify="left")

    if ctx.obj["DUE"]:
        table.add_column("Due")
    if ctx.obj["URGENCY"]:
        table.add_column("Urgency", justify="center")
    if ctx.obj["EFFORT"]:
        table.add_column("Effort", justify="center")

    for i in todos:
        args = []

        if ctx.obj["ID"]:
            args.append(str(i.id))

        args.append(icon_status(i.status))
        args.append(i.description)

        if ctx.obj["DUE"]:
            args.append(due_string(i.due))

        if ctx.obj["URGENCY"]:
            args.append(str(i.urgency))

        if ctx.obj["EFFORT"]:
            args.append(str(i.effort))

        table.add_row(*args)

    console.print(table, new_line_start=True)


def print_plain_todos(todos: Sequence[Todo]) -> None:
    for i in todos:
        id, status, desc = str(i.id), icon_status(i.status), i.description
        print(id, status, desc)
