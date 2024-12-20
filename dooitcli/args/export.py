from argparse import _SubParsersAction, ArgumentParser, BooleanOptionalAction

from .formatter import format_parser
from ..export.markdown.main import markdown
from ..export.todo_txt.main import todo_txt


def add_shared_args(p: ArgumentParser) -> None:
    p.add_argument(
        "--show",
        action=BooleanOptionalAction,
        default=True,
        help="Print the result to the console",
    )
    p.add_argument("--no-write", action="store_true", help="Don't write to a file")
    p.add_argument(
        "--rich", action="store_true", help="Print and render with the rich library"
    )


def add_markdown_args(subparser: _SubParsersAction) -> None:
    desc = "Export to Markdown"

    md = subparser.add_parser("markdown", help=desc, description=desc, add_help=False)
    md.set_defaults(func=markdown)

    format_parser(md)
    add_shared_args(md)

    # Options:
    fmt = md.add_argument_group("Format", "Extra formatting options.")
    fmt.add_argument(
        "--nonstandard",
        "-N",
        action="store_true",
        help="Use nonstandard Markdown syntax. May not be supported by every platform",
    )
    fmt.add_argument(
        "--dataview",
        action="store_true",
        help="Format for Obsidian's Dataview and Tasks plugins",
    )


def add_todo_txt_args(subparser: _SubParsersAction) -> None:
    desc = "Export to todo.txt"

    tt = subparser.add_parser("todo.txt", help=desc, description=desc, add_help=False)
    tt.set_defaults(func=todo_txt)

    format_parser(tt)
    add_shared_args(tt)


def add_args(subparser: _SubParsersAction) -> None:
    desc = "Export your dooit database to a specified format"

    export = subparser.add_parser(
        "export",
        help=desc,
        description=desc,
        add_help=False,
    )

    format_parser(export)
    add_shared_args(export)

    # Formats:
    export_group = export.add_subparsers(
        title="Formats", metavar="[markdown | todo.txt]"
    )

    add_markdown_args(export_group)
    add_todo_txt_args(export_group)
