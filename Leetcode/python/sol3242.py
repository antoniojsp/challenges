# https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.size = len(grid)
        self.grid = grid

        # creates index with values' locations
        self.index = {}
        for i in range(self.size):
            for j in range(self.size):
                self.index[grid[i][j]] = (i,j)

    def sum_neighbor(self, pos):  # helper function
        suma = 0
        for row, col in pos:
            if (0 <= row < self.size) and (0 <= col < self.size):
                suma+=self.grid[row][col]
        return suma

    def adjacentSum(self, value: int) -> int:
        x, y = self.index[value] # value's loation in the grid
        positions = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        return self.sum_neighbor(positions)

    def diagonalSum(self, value: int) -> int:
        x, y = self.index[value] # value's loation in the grid
        positions = [(x-1,y-1), (x-1,y+1),(x+1, y-1), (x+1,y+1)]
        return self.sum_neighbor(positions)


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)