from datetime import datetime, timedelta


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


def checkbox(args, status: str) -> str:
    """
    Takes the todo's status (pending, completed, or overdue)
    and converts it to a markdown checkbox.
    """

    if status == "overdue":
        if args.nonstandard:
            return "- [!] "
        return "- [ ] (!) "

    if status == "completed":
        return "- [x] "

    return "- [ ] "


def dataview_due(args, date: datetime | None) -> str:
    """
    Formats the due date for Dataview.
    """

    if not date:
        return ""

    dt_format = args.date
    due_date = date.strftime(dt_format)

    return f"  [due:: {due_date}]"


def recurrence(args, recur: timedelta) -> str:
    return ""


def urgency(args, urgency: int) -> str:
    match urgency:
        case 4:
            level = "high"
        case 3:
            level = "medium"
        case 2:
            level = "low"
        case _:
            return ""

    if args.dataview:
        return f"  [priority:: {level}]"
    return f"  (urgency: {level})"


def effort(args, effort: int) -> str:
    if effort == 0:
        return ""

    if args.dataview:
        return f"  [effort:: {effort}]"
    return f"  (effort: {effort})"
