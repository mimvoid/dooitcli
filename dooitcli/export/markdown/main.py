from dooit.api import Workspace, manager
from rich.markdown import Markdown

from ..._rich import console
from .parsers import dooit_to_markdown


def markdown(args) -> None:
    """
    Export to Markdown.
    """

    manager.connect()

    lines = dooit_to_markdown(args, Workspace.all())
    text = "\n".join(lines)

    # Write the Markdown file
    if not args.no_write:
        with open("dooit.md", "w") as f:
            f.write(text)

    if args.show:
        if args.rich:
            console.print(Markdown(text, justify="left"))
        else:
            print(text)
