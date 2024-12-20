from dooit.api import Todo, manager

from ..._rich import console
from .parsers import dooit_to_todotxt


def todo_txt(args) -> None:
    """
    Export to todo.txt.
    """

    manager.connect()

    # Get all todos at root level
    todos = [i for i in Todo.all() if i.nest_level == 0]

    lines = dooit_to_todotxt(todos)

    if not args.no_write:
        with open("todo.txt", "w") as f:
            for i in lines:
                f.write(i + "\n")

    if args.show:
        with open("todo.txt", "r") as f:
            if args.rich:
                console.print(f.read())
            else:
                print(f.read())
