
//https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
class Solution {
public:
    int maximumCount(vector<int>& nums) {

        int negative = 0, positive = 0;
        for(auto i: nums){
            if(i < 0){
                negative++;
            }else if (i > 0){
                positive++;
            }
        }
        return negative > positive ? negative : positive;
    }
};