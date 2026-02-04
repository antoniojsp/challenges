from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        Q = deque()
        rows, cols = len(mat), len(mat[0])
        distance_matrix = [[float('inf')]*cols for _ in range(rows)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    distance_matrix[i][j] = 0
                    Q.append((i,j))

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        while Q:
            r, c = Q.popleft()
            for dr, dc in directions:
                if 0 <= r + dr < rows and 0 <= c + dc < cols: # inf represent the 1s
                     if distance_matrix[r+dr][c+dc] > distance_matrix[r][c] + 1: # i.e inf > center + 1
                        distance_matrix[r+dr][c+dc] = distance_matrix[r][c] + 1 # inf => center + 1
                        Q.append([r+dr,c+dc])

        return distance_matrix
