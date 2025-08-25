# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRows is 1, then the answer is "s"
        if numRows == 1:
            return s

        # Creates matrix to store rows
        matrix = [[] for i in range(numRows)]
        row = 0
        direction = True  # if true, goes down
        for char in s:
            matrix[row].append(char)
            if direction:
                row += 1
            else:
                row -= 1

            if row == numRows - 1 or row == 0:
                direction = not direction  # switch direction

        result = []
        for row in matrix:
            result += row

        return "".join(result)