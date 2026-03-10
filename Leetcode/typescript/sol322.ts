


function coinChange(coins: number[], amount: number): number {
    let coins_sorted = [...coins].sort((a,b) => a - b); // no need to sort but possible
    const dp:number[] = new Array(amount+1).fill(Infinity)
    dp[0] = 0;

    for(let i = 0; i < dp.length; i++){
        for(const coin of coins_sorted){
            if((i - coin) >= 0){ // if the coin is not greater than the amount
                dp[i] = Math.min(dp[i], dp[i - coin] + 1)// calculate which one is minimum, the
            }else{
                break;
            }
        }
    }
    return dp[amount] == Infinity ? -1:dp[amount];

};