
# https://leetcode.com/problems/height-checker/description/?envType=problem-list-v2&envId=array

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_h = sorted(heights)
        i = 0
        count = 0
        for i in range(len(heights)):
            if heights[i] != sort_h[i]:
                count+=1

        return count
