
// https://leetcode.com/problems/climbing-stairs/

function climbStairs(n: number): number {
    if(n <= 1){
        return 1;
    }
    let a = 1;
    let b = 1;
    for(let i = 2; i < n+1; i++){
        const temp = a + b;
        a = b;
        b = temp
    }
    return b
    // const stairs:number[] = new Array(n+1).fill(0);
    // stairs[0] = 1; // position 0 and 1 only required 1 action to reach (0 stand there, 1 one step)
    // stairs[1] = 1;
    // for(let i = 2; i < stairs.length; i++){
    //     stairs[i] = stairs[i-1] + stairs[i-2]
    // }

    // return stairs.at(-1);
};