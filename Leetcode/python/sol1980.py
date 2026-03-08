
# https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        unique = set()
        max_val = (2**len(nums))
        for i in nums:
            unique.add(int(i, 2))
        res = ""
        for i in range(max_val):
            if i not in unique:

                res += bin(i)[2:]
                break
        return res.zfill(len(nums))