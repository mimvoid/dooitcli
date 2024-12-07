from dooit.api import Todo, manager
import click

from ...utils.todo import filter_todos
from ...utils.attributes import get_attrs
from .print import print_pretty_todos, print_plain_todos


@click.command("todos", help="Prints out todos that match an attribute value.")
@click.option("--all", "-a", is_flag=True)
@click.option("--plain", "-p", is_flag=True)
def todos(all: bool, plain: bool) -> None:
    manager.connect()

    if all:
        found_todos = Todo.all()
    else:
        todo_list = Todo.all()

        print()
        attr = input("Attribute: ")
        value = input("Value: ")
        print()

        if attr not in get_attrs(todo_list[0]):
            print(f"Error: {attr} is not a valid todo attribute!")
            return

        found_todos = filter_todos(todo_list, attr, value)

        if len(found_todos) == 0:
            print(f"No todos found with \"{attr} = {value}\"!")
            return

    if plain:
        print_plain_todos(found_todos)
    else:
        print_pretty_todos(found_todos)
