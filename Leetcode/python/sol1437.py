# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-17
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = []
        for i, j in enumerate(nums):
            if j == 1:
                index.append(i)
        for i in range(len(index)-1):
            if (index[i+1] - index[i]) <= k:
                return False
        return True


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zeros = 0
        index = []
        for i, j in enumerate(nums):
            if j == 1:
                index.append(zeros)
                zeros = 0
            else:
                zeros+=1
        return all(i >= k for i in index[1:])


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        for i, j in enumerate(nums):
            if prev < 0 and j == 1:
                prev = i
            elif j == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        return True
