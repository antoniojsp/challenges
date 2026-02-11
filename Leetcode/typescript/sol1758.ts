
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/


function minOperations(s: string): number {
    let ones = 0;
    let zeros = 0;
    for(let i = 0; i < s.length; i++){
        const o = i % 2 == 0 ? "1":"0";
        const z = i % 2 == 0 ? "0":"1";

        if(s[i] !== o){
            ones++;
        }
        if(s[i] !== z){
            zeros++;
        }
    }

    return Math.min(ones,zeros);
};