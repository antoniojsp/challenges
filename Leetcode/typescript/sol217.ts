

// https://leetcode.com/problems/contains-duplicate/description/


function containsDuplicate(nums: number[]): boolean {
    const nums_set:Set<number> = new Set<number>(nums);
    return nums.length != nums_set.size
    // const count:Map<number,number> = new Map<number,number>();

    // for(const i of nums){
    //     count.set(i, (count.get(i) ?? 0) + 1);
    // }

    // for(const [key,freq] of count.entries()){
    //     if(freq >= 2){
    //         return true;
    //     }
    // }
    // return false;

};