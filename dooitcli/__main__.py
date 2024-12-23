from rich import traceback
from .args.main import parser


# Change default traceback to rich's
traceback.install(extra_lines=2)


def main() -> None:
    """
    A CLI companion tool to do with dooit.
    """

    # Get command line arguments with argparse
    ARGS = parser.parse_args()

    ARGS.func(ARGS)  # Execute the specified command


if __name__ == "__main__":
    main()
