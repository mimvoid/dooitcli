"""
General-purpose formatting functions
"""

from datetime import datetime


def due_str(date: datetime | None, datefmt: str, timefmt: str) -> str:
    if not date:
        return ""

    dt_format = datefmt

    if date.hour != 0 or date.minute != 0:
        dt_format += timefmt

    return date.strftime(dt_format)
