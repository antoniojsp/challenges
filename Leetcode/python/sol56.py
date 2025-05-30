# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x :x[0])
        result = [intervals[0]]
        for i in intervals[1:]:
            start, end = result[-1]
            start_n, end_n = i
            if end >= start_n:
                result[-1][1] = max(end_n, end)
            else:
                result.append(i)

        return result
