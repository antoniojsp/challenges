// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

function maximumDifference(nums: number[]): number {
        let res:number = -1; // default result if not results is found
        let minimum:number = nums[0];

        for (let i = 1; i < nums.length; i++){
            if(nums[i] > minimum){
                res = Math.max(res, nums[i] - minimum);
            }else{
                minimum = nums[i];
            }
        }

        return res;
};