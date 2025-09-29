# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count = 0
        for i, j in zip(seats, students):
            count+=abs( i -j)
        return count
