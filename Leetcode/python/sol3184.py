# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        for i in range(len(hours)):
            for j in range( i +1, len(hours)):
                if (hours[i] + hours[j] ) %24 == 0:
                    coun t+ =1

        return count
