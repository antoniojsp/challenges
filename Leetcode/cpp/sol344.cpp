// https://leetcode.com/problems/reverse-string/description/

class Solution {
public:
    // void swap(vector<char>& s, int i, int j){
    //     s[i]^=s[j];
    //     s[j]^=s[i];
    //     s[i]^=s[j];
    // }

    void reverseString(vector<char>& s) {
        int length = s.size();
        for(int i = 0; i<length/2;i++){
            swap(s[i], s[length-1-i]);
        }
    }
};


class Solution {
public:
    void swap(vector<char>& s, int i, int j){
        s[i]=s[i]+s[j];
        s[j]=s[i]-s[j];
        s[i]=s[i]-s[j];
    }

    void reverseString(vector<char>& s) {
        int length = s.size();
        for(int i = 0; i<length/2;i++){
            swap(s, i, length-1-i);
        }
    }
};