from dooit.api import Workspace, manager

from parsers import dooit_to_markdown
from config import SHOW_RESULT


def main() -> None:
    manager.connect()

    lines = dooit_to_markdown(Workspace.all())

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
