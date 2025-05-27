
// https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/1646387762/
class Solution {
public:
    int signFunc(int num){
        int rslt = 0;
        if(num > 0){
            rslt = 1;
        }else if(num < 0){
            rslt = -1;
        }
        return rslt;
    }

    int arraySign(vector<int>& nums) {
        int rslt = 1;
        for(int num:nums){
            if (num == 0){
                return 0;
            }
            rslt*=signFunc(num);
        }

        return rslt;
    }
};