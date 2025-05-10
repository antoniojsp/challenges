//https://leetcode.com/problems/valid-anagram/description/


class Solution {
public:

    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }
        vector<int> index(26, 0);

        for(int i = 0; i < s.size(); i++){
            int idx1 = s[i] - 'a';
            index[idx1]++;
            int idx2 = t[i] - 'a';
            index[idx2]--;
        }

        for(auto i:index){
            if(i != 0){
                return false;
            }
        }
        return true;
    }
};