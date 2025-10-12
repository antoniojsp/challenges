
# https://leetcode.com/problems/day-of-the-week/description/

from datetime import datetime
class Solution:
    # 1 de enero de 1971
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        initial_day = 5 #  jan 1 of 1971 is friday
        start_date = datetime.strptime("1971-01-01", "%Y-%m-%d")
        end_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
        days_name = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday"
        }

        day_of_the_week = (initial_day + (end_date - start_date).days)%7
        return days_name[day_of_the_week]
