
//https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/

#include <cctype>
class Solution {
public:

    bool if_digit(string word){
        for(auto i: word){
            if (!isdigit(i)){
                return false;
            }
        }
        return true;
    }

    int maximumValue(vector<string>& strs) {
        int max_val = 0;
        int temp = 0;
        for (auto i: strs){
            if (!if_digit(i)){
                temp = i.size();
            }else{
                temp = stoi(i);
            }
            max_val = max(max_val, temp);
        }

        return max_val;
    }
};