# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rslt = []
        for i in range(len(matrix[0])):
            temp = [matrix[j][i] for j in range(len(matrix))]
            rslt.append(temp)
        return rslt

