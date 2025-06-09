//https://leetcode.com/problems/move-zeroes/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    var replace = 0;
    for(let i = 0; i < nums.length; i++){
        if (nums[i]>0){
            nums[replace] = nums[i];
            replace++;
        }
    }
    for(let i = replace; i < nums.length; i++){
        nums[i] = 0;
    }
};