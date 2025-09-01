# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int, str(num)))
        even = sorted([i for i in num if i% 2 == 0])
        odd = sorted([i for i in num if i % 2 != 0])
        rslt = 0
        for i in num:
            if i % 2 == 0:
                rslt = rslt * 10 + even.pop()
            else:
                rslt = rslt * 10 + odd.pop()
        return rslt

        # num = list(map(int, str(num)))
        # even = [-i for i in num if int(i)%2==0]
        # heapq.heapify(even)
        # odd = [-i for i in num if int(i)%2!=0]
        # heapq.heapify(odd)
        # rslt = 0
        # for i in range(len(num)):
        #     if num[i]%2 == 0:
        #         rslt = rslt*10  + -heapq.heappop(even)
        #     else:
        #         rslt = rslt*10  + -heapq.heappop(odd)
        # return rslt






