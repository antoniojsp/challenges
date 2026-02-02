//https://leetcode.com/problems/maximum-subarray/

function maxSubArray(nums: number[]): number {
    let currMax:number = nums[0];
    let maximum:number = nums[0];

    for(let i = 1; i < nums.length;i++){
        let num:number = nums[i]
        currMax += num;
        if (currMax < num){
            currMax = num;
        }
        maximum = Math.max(currMax, maximum);
    }
    return maximum;
};