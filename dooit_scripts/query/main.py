from dooit.api import Todo, manager

from ..utils.todo import filter_todos


def main() -> None:
    manager.connect()

    todos = Todo.all()

    print("")
    attr = input("Property: ")
    value = input("Value: ")
    print("")

    filtered_todos = filter_todos(todos, attr, value)

    for i in filtered_todos:
        print(i.description)


if __name__ == "__main__":
    main()
