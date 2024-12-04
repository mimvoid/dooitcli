from dooit.api import Todo


def filter_todos(todos: list[Todo], attr: str, value) -> list[Todo]:
    result = []

    # Santitize string with case insensitive match
    fmt_value = str(value).strip().lower()

    for todo in todos:
        todo_value = getattr(todo, attr)
        fmt_todo_value = str(todo_value).strip().lower()

        if fmt_todo_value == fmt_value:
            result.append(todo)

    return result


def recurse_todo(todo: Todo) -> list[Todo]:
    result = [todo]

    if len(todo.todos) > 0:
        for child in todo.todos:
            result += recurse_todo(child)

    return result
