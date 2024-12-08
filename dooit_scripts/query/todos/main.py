from dooit.api import Todo, manager
import click

from ...utils.todo import filter_todos
from ...utils.inspect import get_attrs
from .print import print_pretty_todos, print_plain_todos


@click.command("todos", help="Prints out todos that match an attribute value.")
@click.option("--all", "-a", is_flag=True)
@click.option("--plain", "-p", is_flag=True)
@click.option("--no-header", is_flag=True)
@click.option(
    "--name",
    "-n",
    type=click.Choice(list(get_attrs(Todo)), case_sensitive=False),
    prompt=True,
    help="Name of the attribute or property",
)
@click.option(
    "--value", "-v", prompt=True, help="The value of the attribute to filter by."
)
@click.pass_context
def todos(ctx, name, value, no_header: bool, all: bool, plain: bool) -> None:
    manager.connect()

    ctx.ensure_object(dict)
    ctx.obj["HEADER"] = not no_header

    if all:
        found_todos = Todo.all()
    else:
        found_todos = filter_todos(Todo.all(), name, value)

        if len(found_todos) == 0:
            print(f"No todos found with {name} of value {value}!")
            return

    if plain:
        print_plain_todos(found_todos)
    else:
        print_pretty_todos(found_todos)
