//https://leetcode.com/problems/longest-substring-without-repeating-characters/description/ /


/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {

    var unique = new Set()
    var l = 0;
    var max_count = 0;
    for(let i = 0; i<s.length; i++){
        console.log(unique)
        while(unique.has(s[i])){
            unique.delete(s[l]);
            l++;
        }
        unique.add(s[i]);
        var current = i - l + 1;
        max_count = max_count > current ? max_count:current;
    }
    return max_count;
};