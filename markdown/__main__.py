from dooit.api import Workspace, manager
from parsers import parse_workspaces

from config import SHOW_RESULT


def main() -> None:
    manager.connect()

    lines = parse_workspaces(Workspace.all())

    # Write the Markdown file
    f = open("dooit.md", "w")

    for i in lines:
        f.write(i + "\n")

    f.close()

    if SHOW_RESULT:
        # Print new file contents
        f = open("dooit.md", "r")

        print(f.read())

        f.close()


if __name__ == "__main__":
    main()
