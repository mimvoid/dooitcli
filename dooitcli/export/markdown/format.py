import datetime
import click


def heading(nest_level: int, text: str) -> str:
    """
    Should take in a Workspace object's nest_level and description text.

    Returns a Markdown heading based on the nest_level, or bold text
    if greater than 6, Markdown's smallest heading size.
    """

    if nest_level <= 6:
        hashes = "#" * (nest_level + 1)
        return f"{hashes} {text}"

    return f"**{text}**"


@click.pass_context
def checkbox(ctx, status: str) -> str:
    """
    Takes the todo's status (pending, completed, or overdue)
    and converts it to a markdown checkbox.
    """

    if status == "overdue":
        if ctx.obj["NONSTANDARD"]:
            return "- [!] "
        else:
            return "- [ ] (!) "

    if status == "completed":
        return "- [x] "

    return "- [ ] "


@click.pass_context
def dataview_due(ctx, date: datetime.datetime | None) -> str:
    """
    Formats the due date for Dataview.
    """

    if not date:
        return ""

    dt_format = ctx.obj["DATE"]
    due_date = date.strftime(dt_format)

    return f"  [due:: {due_date}]"


@click.pass_context
def recurrence(ctx, recur: datetime.timedelta) -> str:
    return ""


@click.pass_context
def urgency(ctx, urgency: int) -> str:
    match urgency:
        case 4:
            level = "high"
        case 3:
            level = "medium"
        case 2:
            level = "low"
        case _:
            return " "

    if ctx.obj["DATAVIEW"]:
        return f"  [priority:: {level}]"
    return f"  (urgency: {level})"


@click.pass_context
def effort(ctx, effort: int) -> str:
    if effort == 0:
        return ""

    if ctx.obj["DATAVIEW"]:
        return f"  [effort:: {effort}]"
    return f"  (effort: {effort})"
