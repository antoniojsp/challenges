
//  https://leetcode.com/problems/check-balanced-string/

/**
 * @param {string} num
 * @return {boolean}
 */
var isBalanced = function(num) {

    var suma = 0;

    for(let i = 0; i<num.length; i++){
        if(i%2 == 0){
            suma+=parseInt(num[i]);
        }else{
            suma-=parseInt(num[i]);
        }
    }

    return !suma;

};