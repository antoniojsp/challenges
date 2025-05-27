
// https://leetcode.com/problems/sum-of-good-numbers/description/

class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int sum = 0;
        int length = nums.size();
        for(auto i = 0; i < length; i++){
            int left = i-k;
            int right = i+k;
            bool is_good = true;

            if(left >= 0 && nums[i] <= nums[left]){
                is_good = false;
            }
            if(right < length && nums[i] <= nums[right]){
                is_good = false;
            }

            if(is_good){
                sum+=nums[i];
            }

        }
        return sum;
    }
};