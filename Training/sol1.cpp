//https://leetcode.com/problems/two-sum/description/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++){
            int needs = target - nums[i];
            auto end = seen.find(needs);
            if(end != seen.end()){
                return {i, seen[needs]};
            }
            seen.insert({nums[i], i});
        }
        return {};
    }
};