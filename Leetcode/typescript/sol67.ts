
//https://leetcode.com/problems/add-binary/description/


function addBinary(a: string, b: string): string {
    const length = Math.max(a.length, b.length);
    a = a.padStart(length, "0");
    b = b.padStart(length, "0");
    let remainder:number = 0;
    const result: number[] = [];
    for(let i = length-1; i >=0; i--){
        let sum:number = remainder + parseInt(a[i]) + parseInt(b[i]);
        let digit:number = sum % 2;
        remainder = Math.floor(sum/2)
        result.push(digit)
        // if(1 >= sum){
        //     result.push(sum)
        //     remainder = 0;
        // }else if(sum === 2){
        //     result.push(0)
        //     remainder = 1;
        // }else{
        //     result.push(1)
        //     remainder = 1
        // }
    }
    if(remainder === 1){
        result.push(1)
    }
    result.reverse();
    return result.join("")
};