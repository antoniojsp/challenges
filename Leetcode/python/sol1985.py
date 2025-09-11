#  https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/solutions/7178653/super-simple-maybe-too-simple-by-antonio-4p8y/
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x :int(x), reverse=True)
        return nums[ k -1]
