# https://leetcode.com/problems/excel-sheet-column-title/description/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        while 0 < columnNumber:
            remainder = columnNumbe r %26
            result.append(abc[remainde r -1])
            if remainder == 0:
                columnNumber = (columnNumber - 1 )/ /26
            else:
                columnNumbe r// =26
        result.reverse()
        return "".join(result)






