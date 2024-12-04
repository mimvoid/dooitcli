import click
from .query.main import query
from .export.main import export


@click.group
def main():
    """
    A collection of Python scripts to do with dooit.
    This is currently just a quick and dirty cli implementation with click.
    """


main.add_command(query)
main.add_command(export)


if __name__ == "__main__":
    main()
