# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
class Solution:
    def rotate90(self, matrix):
        for i in range(len(matrix)):
            for j in range( i +1, len(matrix[0])):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()
        return matrix

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if self.rotate90(mat) == target:
                return True
        return False

