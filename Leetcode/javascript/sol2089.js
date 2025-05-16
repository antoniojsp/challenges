
// https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
        nums.sort((a, b) => a - b);
        var size = nums.length;
        var rslt = [];
        console.log(nums);
        for(let i = 0; i < size; i++){
            if (nums[i] == target){
                rslt.push(i);
            }
        }
        return rslt;

};