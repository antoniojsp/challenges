# https://leetcode.com/problems/equal-score-substrings/description/
class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(i) - ord('a') + 1 for i in s)
        left = 0
        for i in range(len(s)):
            left += ord(s[i]) - ord('a') + 1
            if total-left == left:
                return True
        return False
        # left = []
        # right = []
        # for i in range(len(s)):
        #     val1 = ord(s[i]) - ord('a') + 1
        #     if not left:
        #         left.append(val1)
        #     else:
        #         left.append(left[-1]+val1)

        #     val2 = ord(s[len(s) - 1 - i]) - ord('a') + 1
        #     if not right:
        #         right.append(val2)
        #     else:
        #         right.append(right[-1]+val2)

        # for i in range(len(left)-1):
        #     if left[i] == right[len(right)-i-2]:
        #         return True

        # return False




