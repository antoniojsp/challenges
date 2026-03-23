

// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description/

const twoSmallestExcludingFirst = (nums) => {
    let min1 = Infinity;
    let min2 = Infinity;
    for(let i = 1; i < nums.length; i++){
        const num = nums[i]
        if(num < min1){
            min2 = min1;
            min1 = num;
        }else if (num < min2){
            min2 = num;
        }
    }
    return [min1, min2]
}

function minimumCost(nums: number[]): number {
    let first:number = nums[0]; // always take the first element
    const [second, third] = twoSmallestExcludingFirst(nums) // two first elements of the others, which are the minimuym without conmsidering the first element-
    return first + second + third;
};