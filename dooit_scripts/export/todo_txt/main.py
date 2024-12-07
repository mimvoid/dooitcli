from dooit.api import Todo, manager
import click

from .parsers import dooit_to_todotxt
from ..._vars import SHOW_RESULT


@click.command()
def todo_txt() -> None:
    """
    Export to todo.txt.
    """

    manager.connect()

    # Get all todos at root level
    todos = [i for i in Todo.all() if i.nest_level == 0]

    lines = dooit_to_todotxt(todos)

    with open("todo.txt", "w") as f:
        for i in lines:
            f.write(i + "\n")

    if SHOW_RESULT:
        with open("todo.txt", "r") as f:
            print(f.read())
