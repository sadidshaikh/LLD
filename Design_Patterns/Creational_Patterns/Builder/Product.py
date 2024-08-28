from typing import Any


class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {','.join(self.parts)}", end="")
