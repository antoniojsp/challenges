
//https://leetcode.com/problems/shuffle-string/


/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let arr = Array(indices.length).fill("")
    indices.forEach(
        (item, idx) =>
            arr[item] = s[idx]
    )
    return arr.join("");
};