

// https://leetcode.com/problems/binary-gap/description/

// const decimalToBinary = (num: number):number[] =>{
//     const res:number[] = [];
//     while(0 < num){
//         res.push(num%2);
//         num=Math.trunc(num/2);
//     }
//     return res.reverse();
// }


function binaryGap(n: number): number {
    let longest:number = 0;
    let curr: number = 0;
    let oneSeen:boolean = false;
    while(n > 0){
        let bit = n&1;
        if(bit == 1){
            longest = Math.max(longest, curr);
            curr = 1;
            oneSeen = true;
        }else if(oneSeen){
            curr++;
        }
        n >>=1;
    }
    return longest;
    // const binary:number[] = decimalToBinary(n);
    // let longest:number = 0;
    // let curr:number = 0;
    // for(const bit of binary){
    //     console.log(bit, longest, curr)
    //     if(bit == 1){
    //         longest = Math.max(longest, curr);
    //         curr = 1;
    //     }else{
    //         curr++;
    //     }
    // }
    // return longest;
};