
# https://leetcode.com/problems/day-of-the-year/description/


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
        days  = [31, 29 if leap_year else 28, 31, 30,31,30, 31, 31,30,31,30,31]
        result = 0
        for i in range(month-1):
            result += days[i]
        return result + day
