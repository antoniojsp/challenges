# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        abc_values = {"a" :1,
                      "b" :2,
                      "c" :3,
                      "d" :4,
                      "e" :5,
                      "f" :6,
                      "g" :7,
                      "h" :8}

        value = abc_values[coordinates[0]] + int(coordinates[1])
        return valu e % 2! =0

