# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set((i for i in jewels))
        rslt = 0
        for i in stones:
            if i in jewels:
                rslt+=1

        return rslt

