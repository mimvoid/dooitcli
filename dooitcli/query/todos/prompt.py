from typing import Any
from datetime import datetime, timedelta
import dateutil.parser

from rich.prompt import Prompt
from rich.text import Text

from ...utils.inspect import todo_opts, to_bool
from ..._rich import console


def prompt_name() -> str:
    console.print(
        "Choose one of the following attributes or properties:", new_line_start=True
    )

    console.print("\nAttributes", style="bold")
    for k in todo_opts.input_attr:
        console.print(
            Text(k, style="green"),
            Text(todo_opts.get_type_str(k), style="magenta"),
        )

    console.print("\nProperties", style="bold")
    for k in todo_opts.input_prop:
        try:
            console.print(
                Text(k, style="green"),
                Text(todo_opts.get_type_str(k), style="magenta"),
            )
        except AssertionError:
            console.print(Text(k, style="green"))

    return Prompt.ask(
        Text("\nName", style="cyan"),
        choices=list(todo_opts.input_attr) + list(todo_opts.input_prop),
        show_choices=False,
    )


def valid_name(name: str) -> str:
    if name in todo_opts.input_attr or name in todo_opts.input_prop:
        return name

    console.error(f"'{name}' is not a valid attribute or property.")
    return prompt_name()


def prompt_value(name: str) -> str:
    text = "Attribute value" if name in todo_opts.attr else "Property value"
    return Prompt.ask(Text(text, style="cyan"))


def valid_value(name: str, value: str) -> Any:
    if value == "None":
        return None

    try:
        # As far as I can tell, nest_level is the only one whose
        # return type couldn't be inspected
        if name == "nest_level":
            return int(value)

        target = todo_opts.get_type(name)

        if issubclass(target, str):
            return value

        if issubclass(target, datetime):
            return dateutil.parser.parse(value)

        # TODO: if issubclass(target_type, timedelta):

        if issubclass(target, bool):
            return to_bool(value)

        if issubclass(target, int):
            return int(value)

        console.error("couldn't process value: %s" % value)
        return valid_value(name, prompt_value(name))
    except Exception:
        console.error("couldn't process value: %s" % value)
        return valid_value(name, prompt_value(name))
