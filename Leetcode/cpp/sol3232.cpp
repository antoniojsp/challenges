//https://leetcode.com/problems/find-if-digit-game-can-be-won/description/

class Solution {
public:
    bool canAliceWin(vector<int>& nums) {

        for(auto i = 0; i<nums.size(); i++){
            if (nums[i]<10){
                nums[i] = - nums[i];
            }
        }

        return reduce(nums.begin(), nums.end(), 0);
    }
};