


class Solution {
public:
    int singleNumber(vector<int>& nums) {

        int rslt = 0;
        for(int i:nums){
            rslt^=i;
        }

        return rslt;
    }
};