import datetime

from dooit.api import Workspace, Todo, manager


manager.connect()

# Fetch all Todo objects
todos = Todo.all()


def fmt_completion(pending: bool) -> str:
    if pending:
        return ""
    return "x "


def fmt_priority(urgency: int) -> str:
    match urgency:
        case 2:
            return "(C) "
        case 3:
            return "(B) "
        case 4:
            return "(A) "
        case _:
            return ""


def fmt_due_date(date: datetime.datetime | None) -> str:
    if not date:
        return ""

    dt_format = "%Y-%m-%d"
    if date.hour != 0 or date.minute != 0:
        dt_format += " %H:%M"

    due_date = date.strftime(dt_format)
    return f" due:{due_date}"


def to_project(workspace: Workspace | None) -> str:
    if not workspace:
        return ""

    project = workspace.description.replace(" ", "-")

    if workspace.nest_level == 0:
        return f" +{project}"

    return to_project(workspace.parent_workspace) + f"_{project}"


def get_sub_todos(children: list[Todo]) -> str:
    """
    Follows dopart format
    https://github.com/inkarkat/todo.txt-cli-ex/blob/master/tests/t2400-dopart.sh
    """

    children_str = ""

    for child in children:
        desc = child.description

        grandchildren = ""
        if len(child.todos) > 0:
            grandchildren = get_sub_todos(child.todos)

        if not child.due:
            children_str += f", {desc}{grandchildren}"
        else:
            due_date = fmt_due_date(child.due)
            children_str += f", ({desc} => due:{due_date}){grandchildren}"

    return children_str


# Write file
todo_txt = open("todo.txt", "w")

for todo in todos:
    if not todo.parent_todo:
        status = fmt_completion(todo.pending)
        priority = fmt_priority(todo.urgency)
        project = to_project(todo.parent_workspace)
        due_date = fmt_due_date(todo.due)

        row = status + priority + todo.description

        if len(todo.todos) > 0:
            row += get_sub_todos(todo.todos) + project + due_date
        else:
            row += project + due_date

        todo_txt.write(row + "\n")

todo_txt.close()

# Print new file contents
new_todo_txt = open("todo.txt", "r")
print(new_todo_txt.read())
