#  https://leetcode.com/problems/pascals-triangle/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: # when numRow get to 1, return [1] inside the result list
            return [[1]]

        rslt = self.generate(numRows - 1)
        prev_row = rslt[-1]
        new_row = [1]
        for i in range(1, len(prev_row)):
            new_row.append(prev_row[ i -1 ] +prev_row[i])

        new_row.append(1)
        rslt.append(new_row)
        return rslt


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        while numRows > 1:
            new_row = [1]
            prev_row = result[-1]
            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])
            new_row.append(1)
            result.append(new_row)
            numRows -= 1
        return result

        # if numRows == 1: # when numRow get to 1, return [1] inside the result list
        #     return [[1]]

        # rslt = self.generate(numRows - 1)
        # prev_row = rslt[-1]
        # new_row = [1]
        # for i in range(1, len(prev_row)):
        #     new_row.append(prev_row[i-1]+prev_row[i])

        # new_row.append(1)
        # rslt.append(new_row)
        # return rslt




