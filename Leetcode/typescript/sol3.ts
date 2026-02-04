

//https://leetcode.com/problems/longest-substring-without-repeating-characters/

function lengthOfLongestSubstring(s: string): number {
    if(s.length <= 1){ // if string len 0 or 1, then that len is the max length
        return s.length;
    }

    let left:number = 0; // track size of windows
    let right:number = 1;
    let unique = new Set<string>(s[left]);
    let max_len:number = 1;
    while(right < s.length){
        while(unique.has(s[right])){ // if right end present in the windows, delete from the left till all are unique
            unique.delete(s[left]);
            left++;
        }
        unique.add(s[right]); // add right
        max_len = Math.max(max_len, unique.size) // check if it's max length
        right++;
    }
    return max_len;
};