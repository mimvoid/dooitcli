from dooit.api import Todo, manager
import click

from ..utils.todo import filter_todos
from ..utils.checkers import is_valid_attr


@click.command("query", help="Prints out todos that match an attribute value.")
def query() -> None:
    manager.connect()

    todos = Todo.all()

    print()
    attr = input("Attribute: ")
    value = input("Value: ")
    print()

    if not is_valid_attr(todos[0], attr):
        print(f"Error: {attr} is not a valid todo attribute!")
        return

    filtered_todos = filter_todos(todos, attr, value)

    if len(filtered_todos) == 0:
        print(f"No todos found with \"{attr} = {value}\"!")
        return

    for i in filtered_todos:
        print(i.description)
