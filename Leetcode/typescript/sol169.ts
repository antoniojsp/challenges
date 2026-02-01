
//https://leetcode.com/problems/majority-element/description/


function majorityElement(nums: number[]): number {
    let count:number = 0;
    let majority:number = nums[0];
    for(const num of nums){
        if(count == 0){
            majority = num
        }
        count += majority === num ? 1 : -1;
        // else if(majority === num){
        //     count++;
        // }else{
        //     count--;
        // }
    }
    return majority
};

