
//https://leetcode.com/problems/neither-minimum-nor-maximum/description/
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {

    var maximum = Math.max(...nums);
    var minimum = Math.min(...nums);
    for(i of nums){
        if (i != maximum && i != minimum){
            return i;
        }
    }

    return -1
};