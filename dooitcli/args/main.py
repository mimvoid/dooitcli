import argparse
from . import query, export


parser = argparse.ArgumentParser(
    prog="dooitcli",
    description="""
        A collection of Python scripts to do with dooit.
        This is currently just a quick and dirty cli
        implementation with argparse.
    """,
)


parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s 0.0.0",
    help="Prints the version and exits.",
)


# Shared args
parser.add_argument("--date", default="%Y-%m-%d", help="Date format for datetime.")
parser.add_argument("--time", default=" %H:%M", help="Time format for datetime.")

toggles = [
    ("--id", "object ID"),
    ("--due", "due date"),
    ("--recurrence", "recurrence"),
    ("--urgency", "urgency"),
    ("--effort", "effort")
]

for arg, desc in toggles:
    parser.add_argument(
        arg,
        action=argparse.BooleanOptionalAction,
        default=True,
        help=f"Include the {desc} in the output."
    )


subparsers = parser.add_subparsers()

query.add_args(subparsers)
export.add_args(subparsers)


ARGS = parser.parse_args()
