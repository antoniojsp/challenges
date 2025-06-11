

// https://leetcode.com/problems/pascals-triangle/
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {

    var result = [[1]];
    while (numRows > 1){
        var prev_row = result[result.length - 1];
        var new_row = [1];
        for(let i = 1; i < prev_row.length; i++){
            new_row.push(prev_row[i]+prev_row[i-1]);
        }
        new_row.push(1);
        result.push(new_row);
        numRows--;
    }
    return result;
};