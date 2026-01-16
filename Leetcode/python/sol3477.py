# https://leetcode.com/problems/fruits-into-baskets-ii/
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = set()
        for fruit in fruits:
            for index in range(len(baskets)):
                if index not in result and fruit <= baskets[index]:
                    result.add(index)
                    break
        return len(fruits) - len(result)



class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
            count = 0
            for fruit in fruits:
                for index, basket in enumerate(baskets):
                    if fruit <= basket:
                        baskets[index] = -1
                        count += 1
                        break
            return len(fruits) - count