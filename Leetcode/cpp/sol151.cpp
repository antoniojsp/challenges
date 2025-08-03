
// https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution {
public:
    string reverseWords(string s) {
        vector<string> temp;
        string word = "";

        for(auto i: s){
            if (i == ' ' && word != ""){
                temp.push_back(word);
                word = "";
            }else if(i != ' '){
                word+=i;
            }
        }

        if (!word.empty()){
            temp.push_back(word);
        }

        ostringstream result;
        for(int i = temp.size()-1; i >= 0; i--){
            result << temp[i];
            if (i != 0){
                result<< ' ';
            }
        }

        return result.str();
    }
};