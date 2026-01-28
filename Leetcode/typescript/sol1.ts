//https://leetcode.com/problems/two-sum/description/
function twoSum(nums: number[], target: number): number[] {
    let result:number[] = [];
    let seen: {[key: number]: number} = {}
    for (let i = 0; i < nums.length; i++){
        let remainder = target - nums[i];
        if(remainder in seen){
            result.push(i, seen[remainder])
            return result;
        }
        seen[nums[i]] = i;
    }
    return result;
};