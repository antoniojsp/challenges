
# https://leetcode.com/problems/count-binary-substrings/


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        freq = []
        current = s[0]
        count = 0
        for i in s:
            if current != i:
                freq.append(count)
                count=1
                current=i
            else:
                count+=1
        else:
            freq.append(count)

        result = 0
        for i in range(len(freq)-1):
            result += min(freq[i],freq[i+1])
        return result
