from rich.traceback import install
from .args.main import parser


# Change default traceback to rich's
install()


def main() -> None:
    """
    A CLI companion tool to do with dooit.
    """

    # Get command line arguments with argparse
    ARGS = parser.parse_args()

    try:
        ARGS.func(ARGS) # Execute the specified command
    except AttributeError:
        parser.print_help() # No command specified, so print help


if __name__ == "__main__":
    main()
