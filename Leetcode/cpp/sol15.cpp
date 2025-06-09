
//https://leetcode.com/problems/3sum/


class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector <vector<int>> result;
        for(int i = 0; i < nums.size(); i++){
            if(i > 0 && nums[i] == nums[i-1]){ // avpid duplicates
                continue;
            }
            int first_val = nums[i];
            int left = i + 1;
            int right = nums.size() - 1;
            while(left < right){
                if (first_val + nums[left] + nums[right] == 0){
                    while(left < right && nums[left] == nums[left+1]){
                        left++;
                    }
                    while(left < right && nums[right] == nums[right-1]){
                        right--;
                    }

                    vector<int> temp = {first_val, nums[left], nums[right]};
                    result.push_back(temp);
                    left++;
                    right--;
                }else if(first_val + nums[left] + nums[right] > 0){
                    right--;
                }else{
                    left++;
                }
            }
        }


        return result;
    }
};