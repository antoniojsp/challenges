# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
class Solution:
    def ones_in_columns(self, grid :List[List[int]] )->List[int]:
        '''
        Counts the number of ones in each column and
        returns an array with the values
        '''
        return [sum(col) for col in zip(*grid)]

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_size = len(grid)
        col_size = len(grid[0])
        row_ones = [i.count(1) for i in grid] # number of ones in each row
        col_ones = self.ones_in_columns(grid) # number of ones in each column
        row_zero = [row_size - i for i in row_ones] # number of zeros in each row
        col_zero = [col_size - i for i in col_ones] # number of zeros in each column

        result = []
        for i in range(row_size):
            temp = []
            for j in range(col_size):
                diff = (row_ones[i] + col_ones[j]) - (row_zero[i]) - (col_zero[j])
                temp.append(diff)
            result.append(temp)

        return result





