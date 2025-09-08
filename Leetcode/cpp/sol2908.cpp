
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/description/

class Solution {
public:
    int minimumSum(vector<int>& nums) {
        vector<int> left = {nums[0]};
        vector<int> right = {nums[nums.size()-1]};

        for(int i = 1; i < nums.size(); i++){
            left.push_back(min(left.back(), nums[i]));
            right.push_back(min(right.back(), nums[nums.size()-1-i]));
        }

        reverse(right.begin(), right.end());

        int min_sum = INT_MAX;
        for(int i = 1; i < nums.size()-1; i++){
            if(left[i-1] < nums[i] && nums[i] > right[i+1]){
                min_sum = min(left[i-1] + nums[i]+ right[i+1], min_sum);
            }
        }

        return (min_sum == INT_MAX) ? -1:min_sum;
    }
};
