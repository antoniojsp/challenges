

// https://leetcode.com/problems/valid-parentheses/description/
class Solution {
public:
    bool isValid(string s) {

        if (s.size()%2!=0){
            return false;
        }

        vector <char> stack;
        map<char, char> brackets = {{']','['}, {'}','{'}, {')','('}};
        string opening = "[{(";
        for(char bracket:s){
            if(brackets.count(bracket) == 0){
                stack.push_back(bracket);
            }else{
                if(!stack.empty() && stack.back() == brackets[bracket]){
                    stack.pop_back();
                }else{
                    return false;
                }

            }
        }

        return stack.empty();
    }
};