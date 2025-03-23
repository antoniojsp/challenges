

class Solution {
public:
    bool isAcronym(vector<string>& words, string s) {

        string acr = "";

        for (string i: words){
            acr+= i[0];
        }

        return acr == s;

    }
};