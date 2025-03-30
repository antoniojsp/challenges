
# https://leetcode.com/problems/matrix-diagonal-sum/description/?envType=problem-list-v2&envId=array

class Solution:

    def diagonal(self, mat) -> tuple:
        x1, y1 = (0, 0)
        x2, y2 = (len(mat) - 1, 0)
        suma = 0
        i = 0
        while i <= len(mat) - 1:
            suma += (mat[x1 + i][y1 + i] + mat[x2 - i][y2 + i])
            i += 1
        return suma

    def central_value(self, mat):
        size = len(mat)
        return (size // 2, size // 2)

    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        if len(mat) % 2 == 0:
            result = self.diagonal(mat)
        else:
            x, y = self.central_value(mat)
            result = self.diagonal(mat) - mat[x][y]
        return result


