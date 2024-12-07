from dooit.api import Workspace, manager
from rich.markdown import Markdown
import click

from ..._rich import console
from .parsers import dooit_to_markdown
from ..._vars import SHOW_RESULT, RICH_MARKDOWN


@click.command()
def markdown() -> None:
    """
    Export to Markdown.
    """

    manager.connect()

    lines = dooit_to_markdown(Workspace.all())

    # Write the Markdown file
    with open("dooit.md", "w") as f:
        f.writelines(map(lambda i: i + "\n", lines))

    if SHOW_RESULT:
        # Print new file contents
        with open("dooit.md", "r") as f:
            if RICH_MARKDOWN:
                md = Markdown(f.read())
                console.print(md)
            else:
                print(f.read())
