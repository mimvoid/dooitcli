from dooit.api import Todo


def get_targets(todos: list[Todo], attr: str, value: str) -> list[str]:

    targets = []

    # Santitize string with case insensitive match
    fmt_value = value.strip().lower()

    for i in todos:
        todo_value = getattr(i, attr)

        fmt_todo_value = str(todo_value).strip().lower()

        if fmt_todo_value == fmt_value:
            targets.append(i.description)

    return targets
