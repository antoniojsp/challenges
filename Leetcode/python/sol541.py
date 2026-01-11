
# https://leetcode.com/problems/reverse-string-ii/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = []
        reverse = True
        for i in range(0,len(s), k):
            if reverse:
                result.append(s[i:i+k][::-1])
            else:
                result.append(s[i:i+k])
            reverse = not reverse
        return "".join(result)