import click

@click.command("export", help="Exports the dooit database in a given file format.")
@click.option(
    "-f",
    "--format",
    type=str,
    prompt=True,
    help="Format to export as.",
)
def export(format: str) -> None:
    match format:
        case "markdown":
            from .markdown.main import main as cmd

            cmd()
        case "todo.txt":
            print("Oops, this option isn't implemented yet.")
            return
        case _:
            print("Error: Not a supported format.")
