# https://leetcode.com/problems/number-of-days-between-two-dates/description/
from datetime import datetime

def split_date(date):
    year, month, day = date.split("-")
    return datetime(int(year), int(month), int(day))

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        first_date = split_date(date1)
        second_date = split_date(date2)
        return abs(second_date - first_date).days



