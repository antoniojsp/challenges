
# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, left=0, right=None):
            if right is None:
                right = len(s)-1
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(s, left+1, right-1)

        helper(s)
