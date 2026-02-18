
// https://leetcode.com/problems/toggle-light-bulbs/

function toggleLightBulbs(bulbs: number[]): number[] {
    let on:Set<number> = new Set<number>();
    for(const bulb of bulbs){
        if(!on.has(bulb)){
            on.add(bulb);
        }else{
            on.delete(bulb);
        }
    }
    const result = [...on];
    result.sort((a,b) => a - b)
    return result;
};