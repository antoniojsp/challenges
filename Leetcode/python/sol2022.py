# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if n * m != len(original):
            return []
        result = []
        for i in range(0, len(original), n):
            result.append(original[i: i +n])
        return result
        # result = [[] for _ in range(m)]
        # i = 0
        # for row in range(m):
        #     for _ in range(n):
        #         result[row].append(original[i])
        #         i+=1

        # return result
