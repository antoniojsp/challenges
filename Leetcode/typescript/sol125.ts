
// https://leetcode.com/problems/valid-palindrome/description/

function isAlphaNumeric(s: string):boolean{
    return /^[a-z0-9]$/i.test(s);
}

function isPalindrome(s: string): boolean {
    s = s.toLowerCase()
    let array = [];
    for(const i of s){
        if (isAlphaNumeric(i)){
            array.push(i)
        }
    }

    let left = 0;
    let right = array.length - 1;
    for(let i = 0; i < Math.floor(array.length/2); i++){
        if(array[i] !== array[array.length - i - 1]){
            return false
        }
    }

    // let reversed = [...array].reverse()
    // for(let i = 0; i < array.length; i++){
    //     if(array[i] !== reversed[i]){
    //         return false;
    //     }
    // }

    return true;
};