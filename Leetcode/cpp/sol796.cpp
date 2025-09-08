
// https://leetcode.com/problems/rotate-string/

class Solution {
public:
    bool rotateString(string s, string goal) {

        if(s.size() != goal.size()){
            return false;
        }

        string compare = s + s;
        if(compare.find(goal) != string::npos){
            return true;
        }

        return false;

    }
};