
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if value.startswith("="):
            try:
                if value[1:].startswith("'") and value[1:].endswith("'"):
                    return value[2:-1]
                elif value[1:].isdigit():
                    return int(value[1:])
                else:
                    ref_value = self.evaluate(value[1:])
                    if isinstance(ref_value, int):
                        return ref_value
                    else:
                        return "#Circular" if ref_value == value else "#Error"
            except ValueError:
                return "#Error"
        elif value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        elif value.isdigit():
            return int(value)
        else:
            return "#Error"

