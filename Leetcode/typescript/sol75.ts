
//https://leetcode.com/problems/sort-colors/description/


/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    const count = {}
    for(const num of nums){
        if(!(num in count)){
            count[num] = 0;
        };
        count[num]++;
    }
    let curr_pos = 0;
    for(const val of [0, 1, 2]){
        for(let i = 0; i < count[val] || 0; i++){
            nums[curr_pos] = val;
            curr_pos++;
        }
    }
};