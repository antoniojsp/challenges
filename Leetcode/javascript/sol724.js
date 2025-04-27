
//https://leetcode.com/problems/find-pivot-index/description/

/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {

    var left = Array(nums.length);
    left[0] = nums[0];
    for (let i = 1; i< nums.length; i++){
        left[i] = left[i-1] + nums[i];
    }

    var right = Array(nums.length);
    right[nums.length-1] = nums[nums.length-1];
    for (let i = nums.length - 2; i >= 0; i--){
        right[i] = right[i+1] + nums[i];
    }

    for(let i = 0; i<left.length; i++){
        if (left[i] == right[i]){
            return i;
        }
    }

    return -1;
};