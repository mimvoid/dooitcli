from dooit.api import Todo
from rich.table import Table, Column
from rich.text import Text
from rich import box

from ..._rich import console


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


def print_pretty_todos(todos: list[Todo]) -> None:
    table = Table(
        Column("ID", justify="right", style="white"),
        Column("", justify="center"),
        Column("Description", justify="left"),
        box=box.ROUNDED,
    )

    for i in todos:
        args = [str(i.id), icon_status(i.status), i.description]
        table.add_row(*args)

    console.print(table)


def print_plain_todos(todos: list[Todo]) -> None:
    for i in todos:
        id, status, desc = str(i.id), icon_status(i.status), i.description
        print(id, status, desc)
