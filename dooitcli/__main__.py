import click
from rich.traceback import install

from .query.main import query
from .export.main import export


# Change default traceback to rich's
install()


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
# Date formatting
@click.option(
    "--date", default="%Y-%m-%d", show_default=True, help="Date format for datetime."
)
@click.option(
    "--time", default=" %H:%M", show_default=True, help="Time format for datetime."
)
# Toggle todo attributes
@click.option(
    "--id/--no-id", "-i/-I", default=True, help="Include the object id in the output."
)
@click.option(
    "--due/--no-due",
    "-d/-D",
    default=True,
    help="Include the due date in the output.",
)
@click.option(
    "--recurrence/--no-recurrence",
    "-r",
    default=True,
    help="Include recurrence in the output.",
)
@click.option(
    "--urgency/--no-urgency",
    "-u/-U",
    default=True,
    help="Include urgency in the output.",
)
@click.option(
    "--effort/--no-effort",
    "-e/-E",
    default=True,
    help="Include effort in the output.",
)
@click.pass_context
def main(
    ctx,
    date: str,
    time: str,
    id: bool,
    due: bool,
    recurrence: bool,
    urgency: bool,
    effort: bool,
):
    """
    A collection of Python scripts to do with dooit.
    This is currently just a quick and dirty cli implementation with click.
    """

    ctx.ensure_object(dict)

    # Add time formats to context
    ctx.obj["DATE"] = date
    ctx.obj["TIME"] = time

    # Add toggles to context
    ctx.obj["ID"] = id
    ctx.obj["DUE"] = due
    ctx.obj["RECURRENCE"] = recurrence
    ctx.obj["URGENCY"] = urgency
    ctx.obj["EFFORT"] = effort


main.add_command(query)
main.add_command(export)


if __name__ == "__main__":
    main(obj={})
