# https://leetcode.com/problems/find-the-k-or-of-an-array/description/
class Solution:

    def findKOr(self, nums: List[int], k: int) -> int:
        bin_length = max(nums).bit_length()
        table = []
        for i in nums:
            table.append(f"{i:0{bin_length}b}")
        count = []
        for i in zip(*table):
            count.append("1" if i.count("1") >= k else "0")
        return int("".join(count), 2)

