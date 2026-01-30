
// https://leetcode.com/problems/valid-anagram/

const counter = (word:string) => {
    const obj = {};
    for(let i of word){
        if(!(i in obj)){
            obj[i] = 0;
        }
        obj[i]++;
    }
    return obj;
}

function isAnagram(s: string, t: string): boolean {
    if(s.length !== t.length){
        return false;
    }

    const s_obj = counter(s);
    const t_obj = counter(t);

    for(let ch in s_obj){
        if(s_obj[ch] !== t_obj[ch]){
            return false;
        }
    }

    return true;

    // if(s.length !== t.length){
    //     return false;
    // }
    // return s.split("").sort().join() === t.split("").sort().join()
};