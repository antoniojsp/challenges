
# https://leetcode.com/problems/find-the-most-common-response/


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        '''
        No real need to check if responses is empty because the constraints indicate that there is at least 1 response
        '''
        count = defaultdict(int)
        for i in responses:
            for j in set(i):
                count[j]+=1
        max_freq = max(count.values())
        results = min([i for i, j in count.items() if j == max_freq])
        return results