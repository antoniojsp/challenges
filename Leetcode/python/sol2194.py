# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:

        start, end = s.split(":")
        list_of_letters = [chr(i) for i in range(ord(start[0]), ord(end[0]) + 1)]
        rslt = []
        for i in list_of_letters:
            for j in range(int(start[1]), int(end[1]) + 1):
                rslt.append(i + str(j))
        return rslt

