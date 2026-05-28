# https://leetcode.com/problems/reformat-date/description/

class Solution:
    def extract_day(self, date: str) -> str:
        temp = [i for i in date if i.isdigit()]
        return "".join(temp)

    def fill_zeros(self, date):
        date = str(date)
        if len(date) > 1:
            return str(date)

        return f"0{date}"

    def reformatDate(self, date: str) -> str:
        date_parts = date.split(" ")
        months = {month: idx + 1 for idx, month in
                  enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
        print(months)
        day = self.extract_day(date_parts[0])
        month = months[date_parts[1]]
        year = date_parts[2]
        print(day, month, year)
        return f"{year}-{self.fill_zeros(month)}-{self.fill_zeros(day)}"