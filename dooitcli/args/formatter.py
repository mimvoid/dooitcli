import argparse


class CapitalisedHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        if prefix is None:
            prefix = "Usage: "
        return super(CapitalisedHelpFormatter, self).add_usage(
            usage, actions, groups, prefix
        )


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
