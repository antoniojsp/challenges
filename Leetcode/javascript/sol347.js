// https://leetcode.com/problems/top-k-frequent-elements/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    var counter = {};
    for(i of nums){
        if(!(i in counter) ){
            counter[i] = 0;
        }
        counter[i]++;
    }
    const entries = Object.entries(counter);
    entries.sort((a, b) => b[1] - a[1]);
    var result = [];
    for(const i of entries){
        result.push(parseInt(i[0]));
        k--;
        if (k==0){
            break;
        }
    }
    return result
};