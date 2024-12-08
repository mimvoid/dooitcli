from dooit.api import Todo, manager
import click

from ..._rich import console
from .parsers import dooit_to_todotxt


@click.command()
@click.option(
    "--show-result/--no-show-result",
    "-s/-S",
    default=True,
    help="Print the resulting file.",
)
@click.option("--no-write", is_flag=True, help="Don't output a file.")
@click.option("--rich", is_flag=True, help="Render with some highlighting through the rich library.")
@click.pass_context
def todo_txt(ctx, show_result: bool, no_write: bool, rich: bool) -> None:
    """
    Export to todo.txt.
    """

    manager.connect()

    # Get all todos at root level
    todos = [i for i in Todo.all() if i.nest_level == 0]

    lines = dooit_to_todotxt(todos)

    if not no_write:
        with open("todo.txt", "w") as f:
            for i in lines:
                f.write(i + "\n")

    if show_result or ctx.obj["SHOW_RESULT"]:
        with open("todo.txt", "r") as f:
            if rich:
                console.print(f.read())
            else:
                click.echo_via_pager(f.read())
