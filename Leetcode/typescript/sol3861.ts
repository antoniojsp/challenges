
//https://leetcode.com/problems/minimum-capacity-box/description/

function minimumIndex(capacity: number[], itemSize: number): number {
    let minimum = Infinity;
    let result = -1;
    for (let i = 0; i < capacity.length; i++){
        if(itemSize <= capacity[i] && minimum > capacity[i]){
            minimum = Math.min(minimum, capacity[i])
            result = i;
        }
    }
    return result
};