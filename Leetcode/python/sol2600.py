
# https://leetcode.com/problems/k-items-with-the-maximum-sum/description/?envType=problem-list-v2&envId=greedy


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ones = min(k, numOnes)
        k -= ones
        zero = min(k, numZeros)
        k -= zero
        neg = min(k, numNegOnes)
        return ones - neg



        # bag = 0
        # for _ in range(numOnes):
        #     if k == 0:
        #         break
        #     bag+=1
        #     k-=1
        # for _ in range(numZeros):
        #     if k == 0:
        #         break
        #     k-=1
        # for _ in range(numNegOnes):
        #     if k == 0:
        #         break
        #     bag+=-1
        #     k-=1
        # return bag