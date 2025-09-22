//https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2025-09-22

class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> count;
        for(auto i:nums){
            count[i]++;
        }
        int max_freq = 0;
        for (auto i:count){
            max_freq = max(max_freq, i.second);
        }
        int result = 0;
        for (auto i:count){
            if (i.second == max_freq){
                result+= i.second;
            }
        }

        return result;
    }
};