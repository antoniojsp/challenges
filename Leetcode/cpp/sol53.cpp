// https://leetcode.com/problems/maximum-subarray/


class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int max_current = nums[0];
        int max_ending = nums[0];

        for (int i = 1; i < nums.size(); i++){
            max_ending = max(max_ending + nums[i], nums[i] );
            max_current = max(max_current, max_ending);
        }

        return max_current;
    }
};