//https://leetcode.com/problems/house-robber/

function rob(nums: number[]): number {
    let prev1 = 0;
    let prev2 = 0;

    for (const i of nums){
        const curr = Math.max(prev1, prev2+i);
        prev2=prev1;
        prev1=curr;
    }

    return prev1;

    // if (nums.length <= 2){ //
    //     return Math.max(...nums);
    // }
    // nums[1] = Math.max(nums[0], nums[1])
    // for(let i = 2; i < nums.length; i++){
    //     nums[i] = Math.max(nums[i-1], nums[i]+nums[i-2]);
    // };

    // return nums.at(-1);
};


