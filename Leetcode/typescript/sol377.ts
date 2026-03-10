
//https://leetcode.com/problems/combination-sum-iv/description/

function combinationSum4(nums: number[], target: number): number {
    const dp:number[] = Array(target+1).fill(0);
    dp[0] = 1;
    for(let i = 1; i < dp.length; i++){
        for(const num of nums){
            if(i - num >= 0){
                dp[i] += dp[i-num]
            }
        }
    }
    return dp.at(-1);
};