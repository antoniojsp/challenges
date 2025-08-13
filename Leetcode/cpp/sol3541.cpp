//https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/submissions/1707690113/


class Solution {
public:
    unordered_map<char, int> counter(string &s){
        unordered_map<char, int> counter;
        for(auto i: s){
            counter[i]++;
        }
        return counter;
    }

    int maxFreqSum(string s) {
        unordered_map<char, int> freq = counter(s);
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int max_freq_vowels = 0;
        int max_freq_cons = 0;
        for (auto i: freq){
            int curr_freq = i.second;
            if(vowels.contains(i.first)){
                max_freq_vowels = max(max_freq_vowels, curr_freq);
            }else{
                max_freq_cons = max(max_freq_cons, curr_freq);
            }
        }

        return max_freq_vowels + max_freq_cons;
    }
};