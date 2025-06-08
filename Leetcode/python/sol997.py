# https://leetcode.com/problems/find-the-town-judge/description/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge_candidates = [0]*n
        citizen_trust = [0]*n
        for person, candidate in trust: # fill up the 2 lists
            judge_candidates[candidate-1]+=1 #person that is trusted
            citizen_trust[person-1]+=1  #

        idx = 0
        for i, j in zip(judge_candidates, citizen_trust): # now we look for someone who fulfil both requirewments
            if i == n-1 and j == 0:# if someone trust no one, and someone is trusted by n-1 peron, then that's the judge
                return idx+1
            idx+=1

        return -1