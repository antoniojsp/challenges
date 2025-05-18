
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/description/

class Solution {
public:
    string greatestLetter(string s) {

        vector <int> lower(26, 0);
        vector <int> upper(26, 0);

        for(auto i:s){
            int val = i;
            if (val < 'a'){
                int pos = val - 'A';
                lower[pos]++;
            }else{
                int pos = val - 'a';
                upper[pos]++;
            }
        }

        for(int i = lower.size()-1; i >= 0; i--){
            if(lower[i] > 0 && upper[i] > 0){
                char character = (char)('A' + i);
                return string(1, character);
            }
        }

        return "";
    }
};