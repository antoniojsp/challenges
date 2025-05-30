
//https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution {
    public int lengthOfLongestSubstring(String s) {

        if(s.length() == 0){
            return 0;
        }
        int left = 0;
        int right = 0;
        int max_length = 0;
        Set<Character> unique_chars = new HashSet<>();
        while (right < s.length()){
            while(unique_chars.contains(s.charAt(right))){
                unique_chars.remove(s.charAt(left));
                left++;
            }
            unique_chars.add(s.charAt(right));
            int curr_length = right - left + 1;
            max_length = Math.max(curr_length, max_length);
            right++;
        }

        return max_length;
    }
}