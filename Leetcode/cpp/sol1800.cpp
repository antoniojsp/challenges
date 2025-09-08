
// https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }

        int max_sum = nums[0];
        int temp = nums[0];
        int curr = 1;
        while (curr < nums.size()){
            if(nums[curr-1] < nums[curr]){
                temp+=nums[curr];
            }else{
                max_sum = max(max_sum, temp);
                temp = nums[curr];
            }
            curr++;
        }

        return max(temp, max_sum);
    }
};