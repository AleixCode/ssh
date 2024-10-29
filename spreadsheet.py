
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str, visited=None) -> int | str:
        if visited is None:
            visited = set()
        if cell in visited:
            return "#Circular"
        visited.add(cell)
        value = self.get(cell)
        if value.startswith("="):
            if len(value) > 1 and value[1:].isdigit():
                return int(value[1:])
            elif len(value) > 2 and value[1] == "'" and value[-1] == "'":
                return value[2:-1]
            else:
                return self.evaluate(value[1:], visited)
        elif value.isdigit():
            return int(value)
        elif len(value) > 2 and value[0] == "'" and value[-1] == "'":
            return value[1:-1]
        else:
            return "#Error"

