
// https://leetcode.com/problems/digit-frequency-score/


function digitFrequencyScore(n: number): number {
    let solution:number = 0;

    while(n > 0){
        solution += n%10
        n=Math.floor(n/10);
    }
    return solution;
};