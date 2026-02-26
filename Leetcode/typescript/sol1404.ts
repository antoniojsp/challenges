
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26

const binToDecimal = (s) =>{
    let decimal = 0n;
    for(let i = 0; i<s.length;i++){
        decimal = decimal * 2n + BigInt(s[i]);
    }
    return decimal;
}

function numSteps(s: string): number {
    let decimal:bigint = binToDecimal(s);
    let count  = 0;

    while (decimal > 1n){
        count++;
        if(decimal%2n == 0n){
            decimal = decimal/2n;
        }else{
            decimal++;
        }
    }
    return count;
};
