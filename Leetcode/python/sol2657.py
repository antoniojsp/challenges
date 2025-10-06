# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        Since values are distinct, then no need to check if the same index has the same value
        """
        seen = [0 ] *max( A +B)
        rslt = []
        count = 0
        for i, j in zip(A, B):
            seen[i-1]+=1
            if seen[i-1] == 2:
                count+=1
            seen[j-1 ]+=1
            if seen[j-1] == 2:
                count+=1
            rslt.append(count)
        return rslt

