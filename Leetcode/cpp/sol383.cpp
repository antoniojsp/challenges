// https://leetcode.com/problems/ransom-note/description/


class Solution {
public:

    unordered_map<char, int> counter(string str){
        unordered_map<char, int> count;
        for(auto i: str){
            count[i]++;
        }
        return count;
    }

    vector<int> counter_list(string str){
        vector<int> count(26, 0);
        for (int i:str){
            count[i-'a']++;
        }

        return count;
    }

    bool canConstruct(string ransomNote, string magazine) {
        vector<int> note = counter_list(ransomNote);
        vector<int> letters = counter_list(magazine);
        for(int i = 0; i < 26;i++){
            if (!(note[i] <= letters[i])){
                return false;
            }
        }
        return true;

        // for(int i: ransomNote){
        //     int pos = i - 'a';
        //     if (!(note[pos] <= letters[pos])){
        //         return false;
        //     }
        // }


        // unordered_map<char, int> note = counter(ransomNote);
        // unordered_map<char, int> avalaible_letters = counter(magazine);
        // for(int i:temp){
        //     cout << i << ",";
        // }
        // for (auto i:ransomNote){
        //     if(!(note[i]<=avalaible_letters[i])){
        //         return false;
        //     }
        // }
        // return true;
    }
};