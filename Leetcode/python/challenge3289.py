class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        max_value = max(nums)
        storage = [0] * (max_value + 1)
        for i in nums:
            storage[i] += 1

        return [i for i in range(len(storage)) if storage[i] > 1]
