
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/description/


class Solution:
    # without str()
    # def length_int(self, num:int):
    #     if num == 0:
    #         return 1
    #     val = abs(num)
    #     length = 0
    #     while 0 < val:
    #         length+=1
    #         val//=10
    #     return length + 1 if num < 0 else length

    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        rslt = [0]*len(grid[0]) # if grid empetym then it generates a empty list and return it
        for idx, col in enumerate(zip(*grid)):
            max_len = float("-inf")
            for i in col:
                max_len = max(max_len, len(str(i)))
            rslt[idx] = max_len
        return rslt