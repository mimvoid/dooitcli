from dooit.api import Todo

from . import format
from ...utils.todo import recurse_todo


def sub_todos(children: list[Todo]) -> str:
    """
    Follows dopart format
    https://github.com/inkarkat/todo.txt-cli-ex/blob/master/tests/t2400-dopart.sh
    """

    children_str = ""

    for child in children:
        desc = child.description

        if not child.due:
            children_str += f", {desc}"
        else:
            due_date = format.due_date(child.due)
            children_str += f", ({desc} => due:{due_date})"

    return children_str


def dooit_to_todotxt(todos: list[Todo]) -> list[str]:
    lines = []

    for todo in todos:
        status = format.completion(todo.pending)
        priority = format.priority(todo.urgency)

        row = status + priority + todo.description

        if len(todo.todos) > 0:
            for child in todo.todos:
                descendants = recurse_todo(child)
                row += sub_todos(descendants)

        project_name = format.project(todo.parent_workspace)
        due_date = format.due_date(todo.due)

        row += project_name + due_date

        lines.append(row)

    return lines
