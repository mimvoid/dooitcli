import click
from .markdown.main import markdown
from .todo_txt.main import todo_txt


@click.group()
@click.option("--show-result", "-s", is_flag=True, help="Print the resulting file.")
@click.pass_context
def export(ctx, show_result: bool) -> None:
    """
    Export your dooit database into a specified file format.
    """

    ctx.ensure_object(dict)
    ctx.obj["SHOW_RESULT"] = show_result


export.add_command(markdown)
export.add_command(todo_txt)
