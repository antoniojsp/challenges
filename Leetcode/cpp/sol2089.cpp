
//https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {

        sort(nums.begin(), nums.end());
        int size = nums.size();
        vector<int> rslt;
        for(auto i = 0; i < nums.size(); i++){
            if (nums[i] == target){
                rslt.push_back(i);
            }
        }
        return rslt;

    }
};