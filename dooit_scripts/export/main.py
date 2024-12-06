import click

@click.command("export", help="Exports the dooit database in a given file format.")
@click.argument("format", type=str)
def export(format: str) -> None:
    match format:
        case "markdown":
            from .markdown.main import main
            main()
        case "todo.txt":
            print("Oops, this option isn't implemented yet.")
            return
        case _:
            print("Error: Not a supported format.")
