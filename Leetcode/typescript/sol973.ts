//https://leetcode.com/problems/k-closest-points-to-origin/solutions/7548563/solution-easy-by-antoniojsp-9oxs/


function kClosest(points: number[][], k: number): number[][] {
    let index:number[][] = [];
    let i = 0
    for(const [x, y] of points){
        index.push([i, x**2 + y**2])
        i+=1
    }
    index.sort((a,b) => a[1] - b[1]);
    let result = index.slice(0,k).map(x => points[x[0]])
    return result
};

