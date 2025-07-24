import argparse


class CapitalisedHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix="Usage: "):
        return super().add_usage(usage, actions, groups, prefix)


def format_parser(p: argparse.ArgumentParser) -> None:
    p.formatter_class = CapitalisedHelpFormatter

    p._positionals.title = "Arguments"
    p._optionals.title = "Options"

    p.add_argument(
        "-h",
        "--help",
        action="help",
        default=argparse.SUPPRESS,
        help="Show this help message and exit",
    )


def add_toggle_args(p: argparse.ArgumentParser) -> None:
    toggles = p.add_argument_group("Toggles", "Show or hide attributes.")

    for arg in ["--id", "--due", "--recurrence", "--urgency", "--effort"]:
        toggles.add_argument(
            arg,
            action=argparse.BooleanOptionalAction,
            default=True,
        )
