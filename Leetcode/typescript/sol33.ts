
// https://leetcode.com/problems/search-in-rotated-sorted-array/description/
function search(nums: number[], target: number): number {
    let left:number = 0;
    let right:number = nums.length-1;

    while(left <= right){
        const mid = left + Math.floor((right-left)/2);
        if(nums[mid] === target){
            return mid;
        }
        if(nums[left] <= nums[mid]){ //sorted left
            if(nums[left] <= target && target < nums[mid]){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }else{
            if(nums[mid] < target && target <= nums[right]){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
    }

    return -1;
};