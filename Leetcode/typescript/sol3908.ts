
// https://leetcode.com/problems/valid-digit-number/

function validDigit(n: number, x: number): boolean {
    if (n <= 9){
        return false;
    }
    const num_string:string = n.toString();
    return num_string[0] != x.toString() && num_string.includes(x.toString())
    // const stack = [];
    // while(n > 0){
    //     stack.push(n%10);
    //     n = Math.trunc(n/10);
    // }
    // return stack.includes(x) && stack.at(-1) != x;
};