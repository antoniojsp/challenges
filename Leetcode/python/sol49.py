# https://leetcode.com/problems/group-anagrams/


class Solution:

    def string_freq(self, string:str)->str:
        array = [0]*26
        for i in string:
            array[ord(i) - ord('a')]+=1
        return "".join(f"{i} " for i in array)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams = {}
        for i in strs:
            key = self.string_freq(i)
            map_anagrams[key] = map_anagrams.get(key, [])
            map_anagrams[key].append(i)
        return [val for key, val in map_anagrams.items()]