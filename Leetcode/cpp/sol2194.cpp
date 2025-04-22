


//https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/description/

class Solution {
public:
    vector<string> cellsInRange(string s) {

        char start_l = s[0];
        char end_l = s[3];
        char start_num = s[1];
        char end_num = s[4];
        vector<string> rslt;
        for(char i = start_l; i < end_l+1; i++ ){
            for (int j = start_num - '0'; j <= end_num - '0'; j++){
                std::stringstream ss;
                ss << i << j;
                string temp = ss.str();
                rslt.push_back(temp);
            }
        }

        return rslt;
    }
};