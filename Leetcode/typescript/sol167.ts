
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

function twoSum(numbers: number[], target: number): number[] {
    if (numbers.length == 0){
        return [];

    }
    let left:number = 0;
    let right:number = numbers.length-1;

    while(left < right){
        let curr_sum:number = numbers[left] + numbers[right];
        if (curr_sum === target){
            return [left+1, right+1]
        }
        else if(curr_sum < target){
            left++;
        }
        else if(target < curr_sum){
            right--;
        }
    }
    return [];
};