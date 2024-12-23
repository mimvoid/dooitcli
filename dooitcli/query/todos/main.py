from argparse import Namespace

from dooit.api import Todo, manager

from .print import print_pretty_todos, print_plain_todos
from .prompt import prompt_name, valid_name, prompt_value, valid_value
from ...utils.filter import filter_todos
from ..._rich import console


def todos(args: Namespace) -> None:
    manager.connect()

    if args.all:
        found_todos = Todo.all()
    else:
        # Make sure the name and value exist
        if not args.name:
            name = prompt_name()
        else:
            # Check if the name is valid, and prompt if not
            name = valid_name(args.name)

        if not args.value:
            value = valid_value(name, prompt_value(args.name))
        else:
            value = valid_value(name, args.value)

        found_todos = filter_todos(Todo.all(), name, value)

        if not found_todos or len(found_todos) == 0:
            console.failure(f"no todos found with '{name}' of value {value}...")
            return

    if args.plain:
        print_plain_todos(args, found_todos)
    else:
        print_pretty_todos(args, found_todos)
