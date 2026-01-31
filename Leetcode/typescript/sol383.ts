
// https://leetcode.com/problems/ransom-note/description/

const counter = (word) => {
    const count = new Map<string, number>();
    for(const ch of word){
        count.set(ch, (count.get(ch) ?? 0)+1)
    }
    return count;
}

function canConstruct(ransomNote: string, magazine: string): boolean {
    const target = counter(ransomNote)
    const source = counter(magazine)
    for(const [ch, freq] of target.entries()){
        if(!source.has(ch) || target.get(ch) > source.get(ch)){
            return false;
        }
    }
    return true;
};