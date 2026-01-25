
// https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25

function minimumDifference(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let result = Infinity;
    for(let i = 0;i<nums.length-k+1; i++){
        result = Math.min(result, nums[i+k-1] - nums[i])
    }
    return result;
};