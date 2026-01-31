
// https://leetcode.com/problems/ransom-note/description/


const counter = (word:string)=> {
    const count:Map<string, number> = new Map<string, number>();
    for(const ch of word){
        count.set(ch, (count.get(ch) ?? 0)+1)
    }
    return count;
}

function canConstruct(ransomNote: string, magazine: string): boolean {
    const target:Map<string, number>  = counter(ransomNote)
    const source:Map<string, number>  = counter(magazine)
    for(const ch of target.keys()){
        if(!source.has(ch) || target.get(ch) > source.get(ch)){
            return false;
        }
    }
    return true;
};