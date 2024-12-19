import datetime

from dooit.api import Workspace
import click


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


def project(workspace: Workspace | None) -> str:
    if not workspace:
        return ""

    name = workspace.description.replace(" ", "-")

    if workspace.nest_level == 0:
        return f" +{name}"

    return project(workspace.parent_workspace) + f"_{name}"
