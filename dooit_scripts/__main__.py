import click
from rich.traceback import install

from .query.main import query
from .export.main import export


# Change default traceback to rich's
install()


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def main():
    """
    A collection of Python scripts to do with dooit.
    This is currently just a quick and dirty cli implementation with click.
    """


main.add_command(query)
main.add_command(export)


if __name__ == "__main__":
    main()
