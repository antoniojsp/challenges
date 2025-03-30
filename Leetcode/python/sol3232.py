# https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        result: int = 0
        for i in nums:
            if i < 10:
                result+=i
            else:
                result-=i
        return result != 0
