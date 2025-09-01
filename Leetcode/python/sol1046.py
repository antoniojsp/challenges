
# https://leetcode.com/problems/last-stone-weight/description/
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones :List[int] = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_top = -heapq.heappop(stones)
            second_top = -heapq.heappop(stones)
            if first_top != second_top:
                heapq.heappush(stones, - (first_top - second_top))

        return -stones[0] if stones else 0


