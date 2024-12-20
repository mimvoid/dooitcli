import ast

from rich.prompt import Prompt
from rich.text import Text

from ...utils.inspect import todo_opts
from ..._rich import console


def prompt_name() -> str:
    console.print(
        "Choose one of the following attributes or properties:", new_line_start=True
    )

    console.print("\nAttributes", style="bold")
    for k, _ in todo_opts.attributes.items():
        console.print(Text(k, style="green"))

    console.print("\nProperties", style="bold")
    for k in todo_opts.properties:
        try:
            console.print(
                Text(k, style="green"),
                Text(todo_opts.return_type(k).__name__, style="magenta"),
            )
        except AssertionError:
            console.print(Text(k, style="green"))

    return Prompt.ask(
        Text("\nName", style="cyan"),
        choices=list(todo_opts.options),
        show_choices=False,
    )


def valid_name(name: str):
    valid = name in todo_opts.options

    if valid:
        return name

    console.error(f"'{name}' is not a valid attribute or property.")
    return prompt_name()


def prompt_value(name: str):
    if name in todo_opts.attributes:
        prompt = Prompt.ask(Text("Attribute value", style="cyan"))
    else:
        prompt = Prompt.ask(Text("Property value", style="cyan"))

    # Handle the booleans simply, case-insensitive
    if prompt.lower() == "true":
        return True
    if prompt.lower() == "false":
        return False

    try:
        # Try to parse a Python literal from the user input
        return ast.literal_eval(prompt)
    except ValueError:
        # Otherwise, just return the string
        return prompt


def valid_value(value: str):
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    try:
        return ast.literal_eval(value)
    except ValueError:
        return value
