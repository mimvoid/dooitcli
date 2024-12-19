import click

from .todos.main import todos


@click.group()
def query() -> None:
    """
    Filter and print items from your dooit database.
    """
    pass


query.add_command(todos)
