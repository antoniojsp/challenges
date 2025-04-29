// https://leetcode.com/problems/number-of-good-pairs/

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        map <int, int> counter;
        for(auto i:nums){
            if(counter.count(i) == 0){
                counter[i] = 0;
            }else{
                counter[i]++;
            }
        }
        int rslt = 0;
        for(auto i: nums){
            if(counter[i] > 0){
                rslt+=counter[i]--;

            }
        }
        return rslt;

    }
};