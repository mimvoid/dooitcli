from dooit.api import Workspace


def completion(pending: bool) -> str:
    return "" if pending else "x "


def priority(urgency: int) -> str:
    match urgency:
        case 4:
            return "(A) "
        case 3:
            return "(B) "
        case 2:
            return "(C) "
        case _:
            return ""


def project(workspace: Workspace | None) -> str:
    if not workspace:
        return ""

    name = workspace.description.replace(" ", "-")

    if workspace.nest_level == 0:
        return f" +{name}"

    return project(workspace.parent_workspace) + f"_{name}"
