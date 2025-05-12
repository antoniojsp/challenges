# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def array_counter(self, s :str) -> List[int]:
        '''
        Resturns a list from 0 to 25 that keep track the frequencies of each characters
        '''
        temp = [0 ] *26
        for i in s:
            temp[ord(i) - ord('a') ]+=1
        return temp

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        base = self.array_counter(s1)
        count2 = self.array_counter(s2[:len(s1)])
        if base == count2:
            return True

        for i in range(0, len(s2) - len(s1)):
            first = s2[i]
            last = s2[ i +len(s1)]
            count2[ord(first) - ord('a') ]-=1
            count2[ord(last) - ord('a') ]+=1
            if base == count2:
                return True

        return False
