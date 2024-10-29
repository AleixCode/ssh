
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
            try:
                return eval(value[1:], {"__builtins__": None}, self._cells)
            except ZeroDivisionError:
                return "#Error"
            except:
                return "#Error"
        elif value.startswith("'"):
            if value.endswith("'"):
                return value[1:-1]
            else:
                return "#Error"
        else:
            try:
                if '.' in value:
                    return float(value)
                else:
                    return int(value)
            except ValueError:
                return "#Error"

