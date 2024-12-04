import datetime

from config import NONSTANDARD_MARKDOWN


def checkbox(status: str) -> str:
    """
    Takes the todo's status (pending, completed, or overdue)
    and converts it to a markdown checkbox.
    """

    if NONSTANDARD_MARKDOWN and status == "overdue":
        return "- [!]"

    if status == "completed":
        return "- [x] "

    return "- [ ] "


def due_date(date: datetime.datetime | None) -> str:
    """
    Formats the due date and includes the time if present.
    """

    if not date:
        return ""

    dt_format = "%Y-%m-%d"
    if date.hour != 0 or date.minute != 0:
        dt_format += " %H:%M"

    due_date = date.strftime(dt_format)
    return f"  (due: {due_date})"


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
