from argparse import _SubParsersAction, ArgumentParser
from ..export.markdown import main as export_markdown
from ..export.todo_txt import main as export_todo_txt


def add_shared_args(p: ArgumentParser) -> None:
    p.add_argument(
        "--show-result",
        "-s",
        action="store_true",
        help="Print the resulting file to the console.",
    )
    p.add_argument("--no-write", action="store_true", help="Don't write to a file.")
    p.add_argument(
        "--rich", action="store_true", help="Print and render with the rich library."
    )


def add_args(subparser: _SubParsersAction) -> None:
    export = subparser.add_parser(
        "export",
        description="Export your dooit database into a specified file format.",
    ).add_subparsers()

    # Export markdown
    markdown = export.add_parser("markdown")
    markdown.set_defaults(func=export_markdown.markdown)
    add_shared_args(markdown)

    markdown.add_argument(
        "--nonstandard",
        "-N",
        action="store_true",
        help="Use nonstandard Markdown syntax. May not be supported by every platform.",
    )
    markdown.add_argument(
        "--dataview",
        action="store_true",
        help="Format for Obsidian's Dataview and Tasks plugins.",
    )

    # Export todo.txt
    todo_txt = export.add_parser("todo.txt")
    todo_txt.set_defaults(func=export_todo_txt.todo_txt)
    add_shared_args(todo_txt)
