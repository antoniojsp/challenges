//https://leetcode.com/problems/group-anagrams/description/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        for(auto i = 0; i < strs.size(); i++){
            string s = strs[i];
            sort(s.begin(), s.end());
            anagrams[s].push_back(strs[i]);
        }
        vector <vector<string>> rslt;
        for(auto i:anagrams){
            cout << i.first << " ";
            rslt.push_back(i.second);
        }

        return rslt;
    }
};