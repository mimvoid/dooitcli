import argparse
from textwrap import dedent
from . import query, export, formatter


parser = argparse.ArgumentParser(
    prog="dooitcli",
    description=dedent("""
        A CLI companion tool to do with dooit

        This is currently just a quick and dirty implementation with argparse.

        dooit: https://github.com/dooit-org/dooit
        dooitcli: https://github.com/mimvoid/dooitcli
    """),
    add_help=False,
)
formatter.format_parser(parser)


# Commands:
subparsers = parser.add_subparsers(title="Commands", metavar="[COMMAND]")

query.add_args(subparsers)
export.add_args(subparsers)


# Options:
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s 0.0.0",
    help="Show the version and exit",
)


# Datetime:
dt = parser.add_argument_group(
    "Datetime", "String formats for the Python datetime library."
)
dt.add_argument(
    "--date",
    default="%Y-%m-%d",
    help='Date format (default: "%(default)s")',
)
dt.add_argument(
    "--time",
    default=" %H:%M",
    help='Time format (default: " %(default)s")',
)


# Toggles:
toggles = parser.add_argument_group("Toggles", "Show or hide attributes.")

for arg in ["--id", "--due", "--recurrence", "--urgency", "--effort"]:
    toggles.add_argument(
        arg,
        action=argparse.BooleanOptionalAction,
        default=True,
    )
