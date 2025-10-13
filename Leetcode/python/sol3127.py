#  https://leetcode.com/problems/make-a-square-with-the-same-color/description/
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        left_start = [(0 ,0), (0 ,1), (1 ,0), (1 ,1)]
        for x, y in left_start: # check from the four left top starts points
            white = 0
            black = 0
            for i, j in left_start: # from the start point, check left, right and diagonal
                if grid[ x +i][ y +j] == "B":
                    black+=1
                else:
                    white+=1
                if black >= 3 or  white >= 3:
                    return True

        return False



