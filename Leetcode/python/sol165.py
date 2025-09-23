
# https://leetcode.com/problems/compare-version-numbers/solutions/7216781/on-by-antoniojsp-86dy/



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = 0
        while i < len(v1) or i < len(v2):
            val1 = int(v1[i]) if i < len(v1) else 0
            val2 = int(v2[i]) if i < len(v2) else 0
            i+=1
            if val1 ==  val2:
                continue
            elif val1 >  val2:
                return 1
            else:
                return -1
        return 0