# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution:
    def counter_characteres(self, sub_string :str) -> List[int]:
        result = [0 ] *26
        for i in sub_string:
            result[ord(i)-ord('a') ]+=1
        return result

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # it doesn't check for empty string since the constraints 1 <= length
        length = len(p)
        counter_first_sub = self.counter_characteres(s[:length])
        compare = self.counter_characteres(p)
        result = []

        if counter_first_sub == compare: # compare first len(p) from s
            result.append(0)

        for i in range(1, len(s ) -length +1):
            counter_first_sub[ord(s[i -1] ) -ord('a') ]-=1
            counter_first_sub[ord(s[ i +length -1] ) -ord('a') ]+=1
            if counter_first_sub == compare:
                result.append(i)
        return result

