

// https://leetcode.com/problems/sum-of-squares-of-special-elements/
class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int result = 0;
        for(int i = 0; i < nums.size(); i++){
            int n = nums.size();
            if (n%(i+1) == 0){
                result+=(nums[i]*nums[i]);
            }
        }
        return result;
    }
};
