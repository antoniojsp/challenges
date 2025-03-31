
//https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
class Solution {
public:

    int find_index_value(vector<int>& nums){

        int minimo = numeric_limits<int>::max();
        int index = -1;
        for(auto i = 0; i<nums.size(); i++){
            if(minimo > nums[i]){
                minimo = nums[i];
                index = i;
            }
        }

        return index;
    }
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {

        for(auto i = 0; i<k;i++){
            int min = find_index_value(nums);
            nums[min]=nums[min]*multiplier;
        }
        return nums;
    }
};