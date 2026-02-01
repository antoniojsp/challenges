//https://leetcode.com/problems/longest-palindrome/


const counter = (word:string):Map<string, number> => {
    let count:Map<string, number> = new Map<string, number>();
    for(const ch of word){
        count.set(ch, (count.get(ch)??0) + 1);
    }
    return count;
}

function longestPalindrome(s: string): number {
    const ch_freq:Map<string, number> = counter(s);
    let total:number = 0;
    let num_of_odds:number = 0;
    for(const [ch, freq] of ch_freq.entries()){
        if(freq % 2 == 0){
            total += freq;
        }else{
            total+=(freq-1);
            num_of_odds+=1;
        }
    }
    return total + (num_of_odds > 0? 1:0);
};