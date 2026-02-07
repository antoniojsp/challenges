
// https://leetcode.com/problems/3sum/


function threeSum(nums: number[]): number[][] {
    nums.sort((a,b) => a - b);
    const result:number[][] = [];
    for(let i = 0; i < nums.length; i++){
        if(0 < i && nums[i-1] === nums[i]){
            continue;
        }
        let left:number = i+1;
        let right:number = nums.length - 1;
        while(left < right){
            let curr_sum = nums[left] + nums[right] + nums[i];
            if(curr_sum === 0){
                result.push([nums[i], nums[left], nums[right]])
                left++;
                right--;
                while(left <  right && nums[left] === nums[left - 1]){
                    left++;
                }
                while(left <  right && nums[right] === nums[right+1]){
                    right--;
                }
            }else if(0 > curr_sum){
                left++;
            }else{
                right--;
            }
        }
    }

    return result;
};