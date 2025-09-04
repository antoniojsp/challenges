# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/

class Solution:
    def conv_to_minutes(self, time:str):
        hours,minutes = time.split(":")
        return int(hours)*60+int(minutes)

    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0

        curr_time = self.conv_to_minutes(current)
        corr_time = self.conv_to_minutes(correct)

        diff = corr_time - curr_time
        times = [60,15,5,1]
        count = 0

        for minutes in times:
            count+=diff//minutes # i.e 125 minutes % 60 == 2 operations
            diff%=minutes # 2 operations of 60 minutes is 120, leaving 5 minutes , which can be done in one turn

        return count





