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



class Solution {
public:
    unordered_map<string, vector<string>> create_map(vector<string>& str_arr){
        unordered_map<string, vector<string>> anagrams_map;
        for(int i = 0; i < str_arr.size();i++){
            string temp = str_arr[i];
            sort(temp.begin(), temp.end());
            anagrams_map[temp].push_back(str_arr[i]);
        }
        return anagrams_map;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        if(strs.size() <= 1){
            return {strs};
        }

        vector<vector<string>> result;
        unordered_map<string, vector<string>> anagrams_map = create_map(strs);

        for (auto const& [key, arr]:anagrams_map){
            result.push_back(arr);
        }

        return result;
    }
};


class Solution:

    def string_freq(self, string:str)->str:
        array = [0]*26
        for i in string:
            array[ord(i) - ord('a')]+=1
        return "".join(f"{i} " for i in array)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams = {}
        for i in strs:
            key = self.string_freq(i)
            map_anagrams[key] = map_anagrams.get(key, [])
            map_anagrams[key].append(i)
        return [val for key, val in map_anagrams.items()]