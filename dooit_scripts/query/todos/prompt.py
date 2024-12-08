import ast

from rich.prompt import Prompt

from ...utils.inspect import todo_opts
from ..._rich import console


def prompt_name() -> str:
    console.print("Choose one of these attributes or properties:", new_line_start=True)

    console.print("\nAttributes", style="bold")
    console.print(list(todo_opts.attributes.keys()))

    console.print("\nProperties", style="bold")
    console.print(list(todo_opts.properties.keys()))

    return Prompt.ask("\nName", choices=list(todo_opts.options), show_choices=False)


def valid_name(name: str):
    valid = name in todo_opts.options

    if valid:
        return name

    console.print(f"'{name}' is not a valid attribute or property.")
    return prompt_name()


def prompt_value(name: str):
    if name in todo_opts.attributes:
        prompt = Prompt.ask("Attribute value")
    else:
        prompt = Prompt.ask("Property value")

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
    try:
        return ast.literal_eval(value)
    except ValueError:
        return value
