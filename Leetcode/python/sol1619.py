# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        sample = (len(arr) * 5) // 100  # number of elements to remove from the start and from the end
        excluded = arr[sample:len(arr) - sample]

        return sum(excluded) / len(excluded)


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        sample = (len(arr) * 5) // 100  # number of elements to remove from the start and from the end
        # excluded  = arr[sample:len(arr)-sample]
        suma = 0
        for i in range(sample, len(arr) - sample):
            suma += arr[i]

        return suma / (len(arr) - (2 * sample))