# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/?envType=problem-list-v2&envId=string
class Solution:
    def checkString(self, s: str) -> bool:

        for i in range(len(s ) -1):
            if s[i] > s[ i +1]:
                return False

        return True
