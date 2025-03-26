class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen:dict = {}
        for idx, val in enumerate(nums):
            need:int = target - val
            if need in seen:
                return [seen[need], idx]
            else:
                seen[val] = idx

        return []