
// https://leetcode.com/problems/find-the-integer-added-to-array-i/description/?envType=problem-list-v2&envId=array
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var addedInteger = function(nums1, nums2) {

    function suma(arr){
        return arr.reduce((acc, current) => acc+current, 0);
    }
    return (suma(nums2) - suma(nums1))/nums1.length;
};