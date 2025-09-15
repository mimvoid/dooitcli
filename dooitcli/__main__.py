from rich import traceback
from .args.main import parser


# Change default traceback to rich's
traceback.install(extra_lines=2)


def main() -> None:
    """
    A CLI companion tool to do with dooit.
    """

    ARGS = parser.parse_args()  # Get command line arguments with argparse

    if hasattr(ARGS, "func"):
        try:
            ARGS.func(ARGS)  # Execute the specified command
        except KeyboardInterrupt:
            return
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
