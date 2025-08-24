
//https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution {
public:
    bool startswith(string word, string prefix){
        /*
        Just a custom fuction to check the start of the word and see if it matches with the prefix
        better use compare() or substr()
        */
        if(word.size() < prefix.size()){
            return false;
        }

        for(int i = 0; i < prefix.size(); i++){
            if (word[i] != prefix[i]){
                return false;
            }
        }
        return true;
    }

    int countPrefixes(vector<string>& words, string s) {
        int count = 0;
        int word_length = s.size();
        for(string prefix: words){
            cout << s.substr(0, prefix.size())<<endl;
            if (word_length < prefix.size(), s.compare(0, prefix.length(), prefix) == 0){
                count++;
            }
        }

        return count;
    }
};