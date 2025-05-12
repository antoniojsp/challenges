//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1631886004/
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {

    var max_profit = 0;
    var min_price = prices[0];
    for(let i = 1; i < prices.length; i++){
        if(min_price > prices[i]){
            min_price = prices[i];
        }else{
            max_profit = max_profit > prices[i] - min_price?max_profit:prices[i] - min_price;
        }
    }
    return max_profit;
};