from rich.console import Console
from rich.text import Text


class ExtendedConsole(Console):
    def success(self, text: str | Text) -> None:
        self.print(Text("[+] Success:", style="green"), text)

    def warn(self, text: str | Text) -> None:
        self.print(Text("[-] Warning:", style="yellow"), text)

    def failure(self, text: str | Text) -> None:
        self.print(Text("[x] Failure:", style="red"), text)

    def error(self, text: str | Text) -> None:
        self.print(Text("[!] Error:", style="red"), text)


console = ExtendedConsole()
