from argparse import Namespace

from dooit.api import Todo, manager

from ..._rich import console
from .parsers import dooit_to_todotxt


def todo_txt(args: Namespace) -> None:
    """
    Export to todo.txt.
    """

    manager.connect()

    # Get all todos at root level
    todos = list(filter(lambda i: i.nest_level == 0, Todo.all()))

    lines = dooit_to_todotxt(args, todos)
    text = "\n".join(lines)

    if not args.no_write:
        with open("todo.txt", "w") as f:
            f.write(text)

    if args.show:
        if args.no_write:
            output = text
        else:
            with open("todo.txt", "r") as f:
                output = f.read()

        if args.rich:
            console.print(output)
        else:
            print(output)
