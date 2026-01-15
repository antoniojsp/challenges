//https://leetcode.com/problems/mirror-distance-of-an-integer/description/

/**
 * @param {number} n
 * @return {number}
 */
var reverse = (value) =>{
    let res = 0;
    while (0 < value){
        digit = value%10;
        res = res*10+digit;
        value = parseInt(value/10);
    }
    return res;
}

var mirrorDistance = function(n) {
    return Math.abs(n-reverse(n));
};
