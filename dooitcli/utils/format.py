"""
General-purpose formatting functions
"""

from argparse import Namespace
from datetime import datetime


def due_str(args: Namespace, date: datetime | None) -> str:
    if not date:
        return ""

    dt_format = args.date

    if date.hour != 0 or date.minute != 0:
        dt_format += args.time

    return date.strftime(dt_format)
