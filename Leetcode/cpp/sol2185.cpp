class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int count = 0;
        for (string word: words){
            bool add = true;
            for(auto i = 0; i < pref.size() ;i++){
                if (word[i] != pref[i]){
                    add = false;
                    break;
                }
            }
            if (add){
                count++;
            }
        }
        return count;
    }
};