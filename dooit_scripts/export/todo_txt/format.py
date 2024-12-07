from dooit.api import Workspace
import datetime


def completion(pending: bool) -> str:
    if pending:
        return ""
    return "x "


def priority(urgency: int) -> str:
    match urgency:
        case 2:
            return "(C) "
        case 3:
            return "(B) "
        case 4:
            return "(A) "
        case _:
            return ""


def due_date(date: datetime.datetime | None) -> str:
    if not date:
        return ""

    dt_format = "%Y-%m-%d"
    if date.hour != 0 or date.minute != 0:
        dt_format += " %H:%M"

    due_date = date.strftime(dt_format)
    return f" due:{due_date}"


def project(workspace: Workspace | None) -> str:
    if not workspace:
        return ""

    name = workspace.description.replace(" ", "-")

    if workspace.nest_level == 0:
        return f" +{name}"

    return project(workspace.parent_workspace) + f"_{name}"
