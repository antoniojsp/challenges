
//https://leetcode.com/problems/rotate-image/


/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {

    for (let i = 0; i < matrix.length; i++){
        for (let j = i; j < matrix.length; j++){
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];// swap the upper diagonal part to the lower.
        }
        matrix[i].reverse();// reverse
    }

};