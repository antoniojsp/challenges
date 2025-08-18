# https://leetcode.com/problems/toeplitz-matrix/
class Solution:
    def check_diagonal(self ,i, j, matrix :list[list[int]]) -> bool:
        current = matrix[i][j]
        while i < len(matrix) and j < len(matrix[0]):
            if current != matrix[i][j]:
                return False
            i+=1
            j+=1
        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(0, len(matrix[0])):
            if not self.check_diagonal(0, i, matrix):
                return False

        for i in range(1, len(matrix)):
            if not self.check_diagonal(i, 0, matrix):
                return False

        return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

