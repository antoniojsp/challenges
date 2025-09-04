# https://leetcode.com/problems/count-days-spent-together/
class Solution:
    def ith_day(self, date:str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month, day = date.split('-')
        return sum(days[:int(month)-1]) + int(day)

    def mark_dates(self, arrive:int, leave:int, dates:list) -> None:
        for i in range(arrive-1, leave):
            dates[i]+=1

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_arrive  = self.ith_day(arriveAlice)
        alice_left = self.ith_day(leaveAlice)
        bob_arrive = self.ith_day(arriveBob)
        bob_left = self.ith_day(leaveBob)

        days = [0]*365 # passed by reference
        self.mark_dates(alice_arrive, alice_left, days)
        self.mark_dates(bob_arrive, bob_left, days)
        return sum(1 for i in days if i == 2)
