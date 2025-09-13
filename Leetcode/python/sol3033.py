
# https://leetcode.com/problems/modify-the-matrix/description/

class Solution:
    def max_in_col(self, matrix: List[List[int]]) -> List[int]:
        '''
        Returns an array where ith element is the max value of the ith column of grid
        '''
        return [max(i) for i in zip(*matrix)]

    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        max_col = self.max_in_col(matrix) # gets a list with the max values of each column
        answer = [i[:] for i in matrix] # creates a copy of matrix
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == -1:
                    answer[row][col] = max_col[col] # if element is -1, then change with the max value of the column
        return answer