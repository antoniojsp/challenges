
//https://leetcode.com/problems/sqrtx/description/
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    var left = 1, right = x;

    while (left <= right){
        var mid = Math.floor((left+right)/2);
        console.log(left, right, mid)
        if (mid * mid == x){
            return mid;
        }else if (mid*mid > x){
            right = mid - 1;
        }else{
            left = mid + 1;
        }
    }

    return right;
};

