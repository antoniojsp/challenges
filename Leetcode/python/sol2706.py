
# https://leetcode.com/problems/buy-two-chocolates/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first, second = float('inf'), float('inf')
        for i in prices:
            if i < first:
                second = first
                first = i
            elif i < second:
                second = i
        return money - (first+second) if first + second <= money else money

        # 0(n log o)
        # prices.sort()
        # count = 0
        # rslt = money
        # for i in prices:
        #     if money - i >=0:
        #         count+=1
        #         money-=i
        #     if count == 2:
        #         return money

        # return rslt