# https://leetcode.com/problems/row-with-maximum-ones/
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        curr_max = sum(mat[0])
        rslt_index = 0
        for idx, row in enumerate(mat[1:], start=1):
            curr_sum = sum(row)
            if curr_max < curr_sum:
                curr_max = curr_sum
                rslt_index = idx

        return [rslt_index, curr_max]
        # rslt = []
        # for idx, row in enumerate(mat):
        #     rslt.append((idx, sum(row)))
        # return max(rslt, key=lambda x: x[1])


