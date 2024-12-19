from dooit.api import Todo, manager
import click

from ...utils.todo import filter_todos
from ...utils.inspect import todo_opts
from .print import print_pretty_todos, print_plain_todos
from .prompt import prompt_name, valid_name, prompt_value, valid_value


@click.command("todos", help="Prints out todos that match an attribute value.")
@click.option("--all", "-a", is_flag=True)
@click.option("--plain", "-p", is_flag=True)
@click.option("--no-header", is_flag=True)
@click.option(
    "--name",
    "-n",
    type=click.Choice(list(todo_opts.options.keys()), case_sensitive=False),
    help="Name of the attribute or property",
)
@click.option(
    "--value", "-v", help="The value of the attribute to filter by."
)
@click.pass_context
def todos(ctx, name, value, no_header: bool, all: bool, plain: bool) -> None:
    manager.connect()

    ctx.ensure_object(dict)
    ctx.obj["HEADER"] = not no_header

    if all:
        found_todos = Todo.all()
    else:
        if not name:
            # Make sure the name and value exist
            name = prompt_name()
        else:
            # Check if the name is valid, and reprompt if not
            name = valid_name(name)

        if not value:
            value = prompt_value(name)
        else:
            value = valid_value(value)

        found_todos = filter_todos(Todo.all(), name, value)

        if not found_todos or len(found_todos) == 0:
            print(f"Failure: no todos found with {name} of value {value}...")
            return

    if plain:
        print_plain_todos(found_todos)
    else:
        print_pretty_todos(found_todos)
