from argparse import _SubParsersAction
from ..utils.inspect import todo_opts
from ..query.todos.main import todos as query_todos


def add_args(subparser: _SubParsersAction) -> None:
    query = subparser.add_parser(
        "query", description="Filter and print items from your dooit database"
    ).add_subparsers()


    # Query todos
    todos = query.add_parser(
        "todos", help="Prints out todos that match an attribute value."
    )
    todos.set_defaults(func=query_todos)

    todos.add_argument("--all", "-a", action="store_true")
    todos.add_argument("--plain", "-p", action="store_true")
    todos.add_argument("--no-header", action="store_true")

    todos.add_argument(
        "--name",
        "-n",
        choices=todo_opts.options.keys(),
        help="Name of the attribute or property",
    )
    todos.add_argument(
        "--value",
        "-v",
        help="The value of the attribute to filter by.",
    )
