

//https://leetcode.com/problems/reverse-string-prefix/description/
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reversePrefix = function(s, k) {
    let sliced = s.slice(0, k);
    let slicedEnd = s.slice(k)
    let reversed = sliced.split('').reverse().join('');

    return reversed + slicedEnd;
};