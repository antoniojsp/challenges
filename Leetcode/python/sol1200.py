# https://leetcode.com/problems/minimum-absolute-difference/solutions/7266358/defaultdict-by-antoniojsp-5r8x/
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        dict_diff = defaultdict(list)
        for i in range(len(arr ) -1):
            diff = arr[ i +1 ] -arr[i]
            min_diff = min(min_diff, diff)
            dict_diff[diff].append([arr[i], arr[ i +1]])
        return dict_diff[min_diff]


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_diff = float("inf")
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if min_diff > diff:
                result = [[arr[i], arr[i + 1]]]
                min_diff = diff
            elif min_diff == diff:
                result.append([arr[i], arr[i + 1]])
        return result


