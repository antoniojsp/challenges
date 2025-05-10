
// https://leetcode.com/problems/majority-element/description/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0];
        int count = 1;
        for(auto i = 1; i < nums.size(); i++){
            if(count == 0){
                candidate = nums[i];
                count = 1;
            }else if(nums[i] == candidate){
                count++;
            }else{
                count--;
            }
        }
        return candidate;
        }
};
