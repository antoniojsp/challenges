# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/solutions/7091354/0n-by-antoniojsp-5t6s/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        rslt = []
        for i in range(0, len(s), k):
            if i+k <= len(s):
                rslt.append(s[i:i+k])
            else:
                remainder = s[i:]
                length = k - len(remainder)
                rslt.append(remainder + fill*length)
        return rslt