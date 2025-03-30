class Solution {
public:
    int maximo(vector<int>& nums){
        int maximo = 0;
        for (int i: nums){
            if(maximo < i){
                maximo=i;
            }
        }
        return maximo;
    }

    int maximizeSum(vector<int>& nums, int k) {
        int maxi = maximo(nums);
        return (maxi+maxi+k-1)*k/2;
    }
};