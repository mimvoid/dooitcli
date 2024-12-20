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

    ARGS.func(ARGS) # Execute the specified command


if __name__ == "__main__":
    main()
