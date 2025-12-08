# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = defaultdict(int)
        count = 0
        for i in dominoes:
            temp = tuple([min(i), max(i)])
            count += seen[temp]
            seen[temp]+=1
        return count
