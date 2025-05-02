// https://leetcode.com/problems/sort-colors/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    var i = nums.length - 1;
    while(0 <= i){
        let j = 0
        let swapped = false;
        while(j < i){ // 5 10
            if (nums[j] > nums[j+1]){
                nums[j] = nums[j]+nums[j+1] // 15
                nums[j+1] = nums[j] - nums[j+1] // 5
                nums[j] = nums[j] - nums[j+1]

                // let temp = nums[j];
                // nums[j] = nums[j+1]
                // nums[j+1] = temp;
                swapped = true;
            }
            j++;
        }
        i--;
        if(!swapped){
            break;
        }
    }
};