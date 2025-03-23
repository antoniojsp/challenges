/**
 * @param {number[]} nums
 * @return {number}
 */
var smallestEqual = function(nums) {

    for(let idx in nums){
        if(idx % 10 == nums[idx]){

            return parseInt(idx);
        }
    }

    return -1;

};