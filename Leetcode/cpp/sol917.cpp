
// https://leetcode.com/problems/reverse-only-letters/description/

class Solution {
public:

    bool is_alpha(char value){
        /*
        Checks if char is alpha (abc..z). Mostly for simplify syntax
        */
        return std::isalpha(static_cast<unsigned char>(value));
    }

    string reverseOnlyLetters(string s) {
        int start = 0;
        int end =  s.size()-1;

        while(start < end){
            bool l = is_alpha(s[start]);
            bool r = is_alpha(s[end]);
            if(!l){
                start++;
            }
            if(!r){
                end--;
            }
            if((l&&r) ){
                swap(s[start], s[end]);
                start++;
                end--;
            }
        }
        return s;
    }
};


