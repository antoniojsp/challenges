# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(soldiers)

        return [heapq.heappop(soldiers)[1] for i in range(k)]