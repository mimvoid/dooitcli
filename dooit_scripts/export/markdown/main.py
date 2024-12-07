from dooit.api import Workspace, manager
import click

from .parsers import dooit_to_markdown
from ..._vars import SHOW_RESULT


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
            click.echo_via_pager(f.read())
