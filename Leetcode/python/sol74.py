
#  https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:

    def coordinates(self,pos:int, width:int)->tuple:
        return (pos//width, pos%width)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start:int = 0
        end:int = len(matrix)*len(matrix[0])-1

        while start <= end:
            mid:int = (start+end)//2
            x, y = self.coordinates(mid, len(matrix[0])) # mid value in 2d array
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid - 1
            else:
                start = mid +1

        return False