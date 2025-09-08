
# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result:int = 0
        exp = len(columnTitle)-1
        for idx, val in enumerate(columnTitle, start=1):
            result+= (26**exp)*(ord(val)-ord('A')+1)
            exp-=1

        return result