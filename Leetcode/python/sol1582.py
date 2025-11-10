
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        row = [sum(i) for i in mat]
        col = [sum(i) for i in zip(*mat)]
        count = 0
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1 and row[i] == col[j] == 1:
                    count+=1
        return count