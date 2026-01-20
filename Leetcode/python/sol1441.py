# https://leetcode.com/problems/build-an-array-with-stack-operations/
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_set = set(target)
        count = 0
        for i in range(1, n+ 1):
            result.extend(["Push"] if i in target_set else ["Push", "Pop"])
            if i in target_set:
                count += 1
            if len(target) == count:
                break

        return result

