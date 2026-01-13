
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        count = 0
        total = sum(apple)
        capacity.sort(reverse=True)
        for i in capacity:
            if total <= 0:
                break
            count += 1
            total-=i
        return count
