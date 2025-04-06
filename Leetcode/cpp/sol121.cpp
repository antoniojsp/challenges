
//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution {
public:
    int maxProfit(vector<int>& prices) {

        double min_price = INFINITY;
        int max_profit = 0;
        for (int i:prices){
            if(min_price > i){
                min_price = i;
            }else{
                max_profit = max(max_profit, i - (int)min_price);
            }
        }

        return max_profit;
    }
};