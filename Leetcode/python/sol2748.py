# https://leetcode.com/problems/number-of-beautiful-pairs/description/
from math import gcd
def first_digit(n :int) -> int:
    '''
    Takes an INT and returns the most significant digit
    '''
    while n >= 10: n//=10
    return n

def last_digit(n:int) -> int:
    '''
    Takes an INT and returns the least significant digit
    '''
    return n%10

# def are_coprimes(x:int, y:int)->bool:
#     '''
#     check if two values are coprimes
#     '''
#     for i in range(2, min(x, y)):
#         if x%i == 0 and y%i == 0:
#             return False
#     return True

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if gcd(first_digit(nums[i]), last_digit(nums[j])) == 1:
                    ans+=1
        return ans


