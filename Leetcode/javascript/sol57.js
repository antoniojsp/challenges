/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {

    let wasAppended = false;
    const result = [];
    let [start, end] = newInterval;

    for(const [s,e] of intervals){
        console.log(s,e)
        if(e < start){
            result.push([s,e])
        }else if(end < s){
            if(!wasAppended){
                result.push([start, end])
                wasAppended = true;
            }
            result.push([s,e])
        }else{
            start = Math.min(start, s);
            end = Math.max(end, e);
        }
    }

    if(!wasAppended){
        result.push([start, end]);
    }

    return result;

};