#https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
class Solution:
    def greatestLetter(self, s: str) -> str:

        count = ["" ] *26
        for i in s:
            temp = ord(i)
            if temp < ord('a'):
                pos = temp - ord('A')
                if chr(temp) not in count[pos]:
                    count[pos]+=chr(temp)
            else:
                pos = temp - ord('a')
                if chr(temp) not in count[pos]:
                    count[pos]+=chr(temp)

        rslt = ""
        for i, j in enumerate(count[::-1]):
            if len(j) == 2:
                a = list(j)
                a.sort()
                rslt+=a[0]
                break

        return rslt



