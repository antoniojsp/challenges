
// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

function check(nums: number[]): boolean {
    let count:number = 0;
    for(let i = 0; i < nums.length; i++){
        if(nums[i] > nums[(i+1)%nums.length]){ //  check that at mosth there is once contiguos values are decreasing
            count++;
        }
        if(count > 1){
            return false;
        }
    }
    return true;
};