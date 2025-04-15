
//  https://leetcode.com/problems/clear-digits/description/

class Solution {
public:
    string clearDigits(string s) {

        string rslt = "";
        for (char i:s){
            if (!isdigit(i)){
                rslt+=i;
            }else{
                if(!rslt.empty()){
                    rslt.pop_back();
                }
            }
        }
        return rslt;
    }
};