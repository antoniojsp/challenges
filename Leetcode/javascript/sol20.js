

//https://leetcode.com/problems/valid-parentheses/description/
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];
    const brackets = {
        '}':'{',
        ')':'(',
        ']':'['
    };

    for(const char of s){
        if (char in brackets){
            if (stack.length != 0){
                var last_element = stack[stack.length -1];
                if (last_element == brackets[char]){
                    stack.pop();
                }else{
                    return false;
               a }
            }else{
                return false;
            }

        }else{
            stack.push(char);
        }
    }
    return stack.length == 0;
};