# https://leetcode.com/problems/find-the-encrypted-string/
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:

        result: List = ['' ] *len(s)

        for i in range(len(s)):
            position: int = ( i +k ) %len(s)
            result[i] = s[position]

        return "".join(result)
