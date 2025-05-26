
//https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/

class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int half_length = nums.size()/2;
        map <int, int> count;
        for(int num:nums){
            count[num]++;
        }
        int rslt = -1;
        for(auto freq:count){
            if(freq.second == half_length){
                rslt = freq.first;
                break;
            }
        }
        return rslt;
    }
};