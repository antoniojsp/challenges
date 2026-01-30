
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


function maxProfit(prices: number[]): number {
    let minCost = prices[0];
    let maxProfit = 0;
    for(const price of prices){
        // minCost = Math.min(minCost, price);
        minCost = price < minCost ? price:minCost
        // maxProfit = Math.max(maxProfit, price - minCost);
        maxProfit = price - minCost > maxProfit ? price - minCost: maxProfit
    }
    return maxProfit;
};