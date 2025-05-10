
// https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> counter;
        for(int i:nums){
            counter[i]++;
        }
        vector<vector<int>> freq(nums.size()+1);
        for(auto i: counter){
            freq[i.second].push_back(i.first);
        }

        vector <int> rslt;
        int count = 0;

        for(int i = freq.size() - 1; i >= 0; i--){
            if(count == k){
                break;
            }
            for(auto j:freq[i]){
                rslt.push_back(j);
                count+=1;
            }
        }

        return rslt;
    }
};