
// https://leetcode.com/problems/first-letter-to-appear-twice/description/
class Solution {
public:
    char repeatedCharacter(string s) {

        set <char> seen;
        char rslt = '\0';
        for(char c: s){
            if(seen.count(c)){
                rslt = c;
                break;
            }
            seen.insert(c);
        }
        return rslt;
    }
};
