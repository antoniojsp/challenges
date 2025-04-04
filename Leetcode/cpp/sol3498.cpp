# https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution {
public:
    int reverseDegree(string s) {
        int result = 0;
        for(auto i = 0;i<s.size();i++){
            int ord = s[i] - 96;
            result = result + ((27-ord)*(i+1));
        }
        return result;
    }
};