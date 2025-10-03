# https://leetcode.com/problems/earliest-time-to-finish-one-task/
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        """
        Constaints indicate that there is atlest on task with starting time and time spend
        So, no need to check if the list is empty
        """
        return min(sum(task) for task in tasks)
