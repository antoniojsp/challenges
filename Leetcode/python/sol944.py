# https://leetcode.com/problems/delete-columns-to-make-sorted/description/
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for col in range(len(strs[0])):
            prev = chr(0) # absolute lowest
            for row in range(len(strs)): # check if the colum is in order
                if prev > strs[row][col]: # if previous is greater than current, add counter and break.
                    result+=1
                    break
                prev = strs[row][col] # update previous to check next koop

        return result

