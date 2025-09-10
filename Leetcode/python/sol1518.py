# https://leetcode.com/problems/water-bottles/description/
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while numBottles>= numExchange: # when the bottles availables are less than the numExchange, then no more exchange can happe
            new_bott = numBottles//numExchange # full bottles you can get
            remainder = numBottles %numExchange # empty bottles that are not enough to exchange
            total += new_bott  # adding how many bottles you can get so far
            numBottles = new_bott + remainder # update the number of bottles you currently have after exchange

        return total