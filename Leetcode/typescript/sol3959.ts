// https://leetcode.com/problems/check-good-integer/description/


function checkGoodInteger(n: number): boolean {
    let digitSum = 0;
    let squareSum = 0;
    while(n > 0){
        let digit = n%10;
        n = Math.trunc(n/10)
       digitSum+=digit;
       squareSum+=digit**2;
    }
    return  squareSum - digitSum >= 50;
};