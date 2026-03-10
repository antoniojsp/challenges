
//https://leetcode.com/problems/perfect-squares/submissions/1943906527/


function numSquares(n: number): number {
    const dp:number[] = Array(n+1).fill(Infinity);
    dp[0] = 0;
    const squares:number[] = [];
    for(let i = 1; i*i <= n; i++){
        squares.push(i*i);
    }
    for(let i = 1; i <= n; i++){
        for (const num of squares){
            let need:number = i - num;
            if(num > i){
                break;
            }
            dp[i] = Math.min(dp[i], dp[need]+1)

        }
    }
    return dp[n] == Infinity ? -1:dp[n];
};