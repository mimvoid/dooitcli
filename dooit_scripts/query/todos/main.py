from dooit.api import Todo, manager
import click

from ...utils.todo import filter_todos
from ...utils.attributes import get_attrs


@click.command("todos", help="Prints out todos that match an attribute value.")
def todos() -> None:
    manager.connect()

    todo_list = Todo.all()

    print()
    attr = input("Attribute: ")
    value = input("Value: ")
    print()

    if attr not in get_attrs(todo_list[0]):
        print(f"Error: {attr} is not a valid todo attribute!")
        return

    filtered_todos = filter_todos(todo_list, attr, value)

    if len(filtered_todos) == 0:
        print(f"No todos found with \"{attr} = {value}\"!")
        return

    for i in filtered_todos:
        print(i.description)
