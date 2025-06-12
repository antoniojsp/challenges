
# https://leetcode.com/problems/destroying-asteroids/description/

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        max_val = max(asteroids)
        weights = [0]*(max_val+1)
        for i in asteroids: # count sort
            weights[i]+=1

        for i, j in enumerate(weights):
            if mass >= i and j != 0:
                mass+=i*j
            if mass < i:
                return False

        return True

