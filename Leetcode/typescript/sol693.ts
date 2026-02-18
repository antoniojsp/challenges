
// https://leetcode.com/problems/binary-number-with-alternating-bits/?envType=daily-question&envId=2026-02-18

function hasAlternatingBits(n: number): boolean {
    while(0 < n){
        if(n%2 == (Math.trunc(n/2)%2)){
            return false;
        }
        n = Math.trunc(n/2)
    }
    return true;
};