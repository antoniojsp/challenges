
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



const countEvenOdd = (nums:number[]) => {
    let odd = 0;
    let even = 0;
    for(const num  of nums){
        if(num%2 == 0){
            even++;
        }else{
            odd++;
        }
    }
    return [even, odd]
}

function countOppositeParity1(nums: number[]): number[] {
    let [even, odd] = countEvenOdd(nums);
    const result:number[] = []
    for(const num of nums){
        if(num%2 === 0){
            even--;
            result.push(odd)
        }else{
            odd--;
            result.push(even)
        }
    }
    return result;
};