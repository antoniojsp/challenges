
# https://leetcode.com/problems/count-square-sum-triples/description/


class Solution:
    # def binary_square(self, num:int):
    #     start = 1
    #     end = num
    #     while start <= end:
    #         mid = (start+end)//2
    #         if mid*mid == num:
    #             return mid
    #         elif mid*mid < num:
    #             start = mid+1
    #         else:
    #             end = mid-1
    #     return -1

    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                c = sqrt(a**2 + b**2) # or isqrt
                if c.is_integer() and c <=n:
                    count+=2
                # if c != -1 and c <= n:
                #     count+=2 # add 2 because if a**2 + b**2 = c**2 then swapping a and b also gives the same result
        return count
