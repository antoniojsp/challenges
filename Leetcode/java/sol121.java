
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1648417938/

class Solution {
    public int maxProfit(int[] prices) {

        int min_price = prices[0];
        int max_profit = 0;
        for (int i : prices) {
            if(min_price > i){
                min_price = i;
            }
            max_profit = max_profit < i - min_price ? i - min_price:max_profit;

        }
        return max_profit;
    }
}