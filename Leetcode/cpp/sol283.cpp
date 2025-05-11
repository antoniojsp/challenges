

//https://leetcode.com/problems/move-zeroes/description/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        int pos = 0;
        // first, move all the non zero numbers to the beginning of nums
        for(int i = 0; i<nums.size(); i++){
            if(nums[i] != 0){
                nums[pos] = nums[i];
                pos++;
            }
        }
        // then, fill zeros from the last position added
        for(int i = pos; i<nums.size(); i++){
            nums[i] = 0;
        }

    }
};