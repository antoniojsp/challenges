// https://leetcode.com/problems/valid-palindrome/


class Solution {
public:
    bool isPalindrome(string s) {

        string clean_string = "";
        for(auto i:s){
            if(isalnum(i)){
                clean_string+=tolower(i);
            }
        }

        for(int i = 0; i < (int)clean_string.size()/2; i++){
            if(clean_string[i] != clean_string[clean_string.size()-1-i]){
                return false;
            }
        }

        return true;

    }
};