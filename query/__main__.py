from dooit.api import Todo, manager

from utils import get_targets


def main() -> None:
    manager.connect()

    todos = Todo.all()

    print("")
    attr = input("Property: ")
    value = input("Value: ")
    print("")

    target_todos = get_targets(todos, attr, value)

    for i in target_todos:
        print(i)


if __name__ == "__main__":
    main()
