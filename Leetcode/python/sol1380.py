# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minimum = []
        for row in matrix:
            minimum.append(min(row))
        maximum = []
        for col in zip(*matrix):
            max_value =max(col)
            if max_value in minimum:
                maximum = [max_value]

        return maximum
