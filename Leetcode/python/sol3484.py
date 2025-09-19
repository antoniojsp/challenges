# https://leetcode.com/problems/design-spreadsheet/submissions/1776089655/
class Spreadsheet:

    def __init__(self, rows: int):
        self.dictionary = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.dictionary[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.dictionary:
            del self.dictionary[cell]

    def getValue(self, formula: str) -> int:
        x, y = formula.replace("=" ,"").split("+")
        if x[0].isdigit():
            a = int(x)
        else:
            a = self.dictionary[x]

        if y[0].isdigit():
            b = int(y)
        else:
            b = self.dictionary[y]
        return a+ b

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)