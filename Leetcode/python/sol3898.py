class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        rslt = []
        for node in matrix:
            rslt.append(sum(node))
        return rslt