from argparse import _SubParsersAction

from .formatter import format_parser
from ..utils.inspect import todo_opts
from ..query.todos.main import todos as query_todos


def add_todo_args(subparser: _SubParsersAction) -> None:
    desc = "Filter and print todos"

    todos = subparser.add_parser(
        "todos",
        help=desc,
        description=desc
        + "\n \nOfficial dooit documentation of attributes and properties:\nhttps://dooit-org.github.io/dooit/backend/todo",
        add_help=False,
    )
    todos.set_defaults(func=query_todos)
    format_parser(todos)

    # Query:
    query = todos.add_argument_group("Query")
    query.add_argument(
        "--name",
        "-n",
        choices=todo_opts.options.keys(),
        metavar="ATTR",
        help="The attribute or property to filter by",
    )
    query.add_argument(
        "--value",
        "-v",
        help="Value of the attribute or property to filter by",
    )

    # Render:
    render = todos.add_argument_group(
        "Render", "How to print the output to the console."
    )
    render.add_argument(
        "--plain", "-p", action="store_true", help="Print as plain text"
    )
    render.add_argument(
        "--no-header", action="store_true", help="Don't show the table header"
    )


def add_args(subparser: _SubParsersAction) -> None:
    desc = "Filter and print items from your dooit database"

    query = subparser.add_parser(
        "query",
        help=desc,
        description=desc,
        add_help=False,
    )
    format_parser(query)

    # Shared args
    query.add_argument(
        "--all", "-a", action="store_true", help="Show all items, don't filter"
    )

    # Items:
    query_group = query.add_subparsers(title="Items", metavar="[ITEM]")
    add_todo_args(query_group)
