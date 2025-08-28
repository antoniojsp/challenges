# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        First sort,
        Bob is the last player in each turn, so to maximize your coins, first remove bobs coins in ech turn (len(piles)//3) lowest one
        The reminder list, pick the two smallest values of each pair (each reminded pair represent a turn)
        Add up the lowest of each pair
        """
        piles.sort(reverse=True)
        bob_lowest = len(piles )/ /3
        suma = 0
        for i in range(1, len(piles) - bob_lowest, 2):
            sum a+ =piles[i]
        return suma

