# https://leetcode.com/problems/license-key-formatting/description/


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        temp = s.replace("-", "")
        first = len(temp)%k
        result = [temp[0: first]] if first > 0 else []
        for i in range(first, len(temp), k):
            result.append(temp[i:i+k])
        return "-".join(result)