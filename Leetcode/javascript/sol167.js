// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {

    var left = 0;
    var right = numbers.length - 1;
    while (left < right){
        if(numbers[left] + numbers[right] == target){
            return [left+1, right+1];
        }else if (numbers[left] + numbers[right] > target){
            right--;
        }else{
            left++;
        }
    }
    return -1
};