# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0

        for s1, s2 in zip(startTime, endTime):
            if (s1 <= queryTime <= s2):
                count+=1

        return count


