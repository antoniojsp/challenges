
//https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    var suma = nums.reduce((current, next) => current + next);

    return suma%k;
};