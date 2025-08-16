#  https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) == 0: # check for empty strings
            return ""
        rslt = [s[0]] # add first element for the result and to keep
        numbers = 1
        for i in s[1:]:
            if i == rslt[-1]:
                numbers+=1
            else:
                numbers =1
            if numbers < 3:
                rslt.append(i)

        return "".join(rslt)
