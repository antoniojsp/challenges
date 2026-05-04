
// https://leetcode.com/problems/count-indices-with-opposite-parity/description/

function countOppositeParity(nums: number[]): number[] {
    const isEven = (num:number) => {
        return  num%2 == 0;
    }
    const result:number[] = [];
    for(let i = 0; i < nums.length; i++){
        let res:number = 0;
        for(let j = i+1; j < nums.length; j++){
            if(isEven(nums[i]) !==  isEven(nums[j])){
                res++;
            }
        }
        result.push(res);
    }

    return result;
};