from dooit.api import Workspace, manager
from rich.markdown import Markdown
import click

from ..._rich import console
from .parsers import dooit_to_markdown


@click.command()
# Result display
@click.option(
    "--show-result/--no-show-result",
    "-s/-S",
    default=True,
    help="Print the resulting file.",
)
@click.option("--no-write", is_flag=True, help="Don't output a file.")
@click.option("--rich", is_flag=True, help="Print and render with the rich library.")
# Formatting
@click.option(
    "--nonstandard",
    "-N",
    is_flag=True,
    help="Use nonstandard Markdown syntax. May not be supported by every platform.",
)
@click.option(
    "--dataview", is_flag=True, help="Format for Obsidian's Dataview and Tasks plugins."
)
@click.pass_context
def markdown(
    ctx,
    show_result: bool,
    no_write: bool,
    rich: bool,
    nonstandard: bool,
    dataview: bool,
) -> None:
    """
    Export to Markdown.
    """

    manager.connect()

    ctx.ensure_object(dict)
    ctx.obj["NONSTANDARD"] = nonstandard
    ctx.obj["DATAVIEW"] = dataview

    lines = dooit_to_markdown(Workspace.all())
    text = "\n".join(lines)

    # Write the Markdown file
    if not no_write:
        with open("dooit.md", "w") as f:
            f.write(text)

    if show_result or ctx.obj["SHOW_RESULT"]:
        if no_write:
            output = text
        else:
            with open("dooit.md", "r") as f:
                output = f.read()

        if rich:
            console.print(Markdown(output, justify="left"))
        else:
            click.echo_via_pager(output)
