//https://leetcode.com/problems/valid-parentheses/description/

function isValid(s: string): boolean {
    const stack: string[] = [];
    const brackets:{[key:string]:string} = {"}":"{", ")":"(", "]":"["};
    for(let ch of s){
        if(ch in brackets){
            const top = stack.pop();
            if(brackets[ch] !== top){
                return false;
            }
        }else{
            stack.push(ch)
        }
    }
    return stack.length == 0
};