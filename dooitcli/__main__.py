from rich.traceback import install
from .args.main import ARGS


# Change default traceback to rich's
install()


def main() -> None:
    """
    A CLI companion tool to do with dooit.
    """

    print(ARGS)
    print(ARGS.date)
    print(type(ARGS.date))
    ARGS.func(ARGS)


if __name__ == "__main__":
    main()
