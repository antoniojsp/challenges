
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

const numberOnes = (num:number) =>{
    let count = 0;
    while(num > 0){
        count += num & 1;
        num>>=1;
    }
    return count;
}

function sortByBits(arr: number[]): number[] {
    const res = []
    for(let i = 0; i< arr.length; i++){
        res.push([arr[i], numberOnes(arr[i])])
    }
    res.sort((x,y) => {
        if(x[1] === y[1]){
            return x[0] - y[0];
        }
        return x[1]-y[1]
    })

    const solution = res.map(x => x[0]);
    return solution;
};