
//https://leetcode.com/problems/insert-interval/

function insert(intervals: number[][], newInterval: number[]): number[][] {
    let pushed = false;
    const result:[number, number][] = [];
    let [start, end] = newInterval;
    for(const [s, e] of intervals){
        // when the new interval comes before the curr interval
        if(e < start){
            result.push([s,e])
        // when interval comes after
        }else if(end < s){
            if(!pushed){// once is inserted, there is no need to insert again

                result.push([start, end]);
                pushed = true;
            }
            result.push([s, e])
        // merge intervals.
        }else{
                start = Math.min(start, s)
                end = Math.max(end, e)
        }
    }
    if(!pushed){
        result.push([start, end])
    }
    return result;
};