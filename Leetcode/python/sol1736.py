# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
class Solution:
    def maximumTime(self, time: str) -> str:
        hours, minutes = time.split(":")
        hours, minutes = list(hours), list(minutes)

        if hours[0] == "?":
            hours[0] = "2" if hours[1] in "0123?" else "1"

        if hours[1] == "?":
            hours[1] = "3" if hours[0] == "2" else "9"

        if minutes[0] == "?":
            minutes[0] = "5"
        if minutes[1] == "?":
            minutes[1] = "9"

        return "".join(hours +[":" ] +minutes)

