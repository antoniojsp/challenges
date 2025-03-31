# https://leetcode.com/problems/find-center-of-star-graph/description/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0]
        return first if first in edges[1] else second