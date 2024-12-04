from dooit.api import Todo, manager
import click

from ..utils.todo import filter_todos, get_ancestors
from ..utils.checkers import is_valid_attr
from .._vars import INDENT_LEVEL


@click.command("query", help="Prints out todos that match an attribute value.")
def query() -> None:
    manager.connect()

    todos = Todo.all()

    print("")
    attr = input("Attribute: ")
    value = input("Value: ")
    print("")

    if not is_valid_attr(todos[0], attr):
        print(f"Error: {attr} is not a valid todo attribute!")
        return

    filtered_todos = filter_todos(todos, attr, value)

    if len(filtered_todos) == 0:
        print(f"No todos found with \"{attr} = {value}\"!")
        return

    for i in filtered_todos:
        if i.nest_level > 0:
            # for todo in get_ancestors(i)[::-1]:
            #     indent = " " * (todo.nest_level * INDENT_LEVEL)
            #     print(indent + f"({todo.description})")

            indent = " " * (i.nest_level * INDENT_LEVEL)
            print(indent + i.description)
        else:
            print(i.description)
