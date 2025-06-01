
//https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var left = 0;
        var max_length = 0;
        val unique = mutableSetOf<Char>()
        for (index in 0..s.length-1) {
            while(unique.contains(s[index])){
                unique.remove(s[left]);
                left++;
            }
            unique.add(s[index]);
            max_length = maxOf(max_length, index - left + 1);
        }

        return max_length;
    }
}