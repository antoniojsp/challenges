
// https://leetcode.com/problems/climbing-stairs/

class Solution {
public:
    int climbStairs(int n) {
        if(n == 1){
            return n;
        }

        vector<int> dp = {1,1};
        for(int i = 2; i<n+1; i++){
            int temp = dp[i-1] + dp[i-2];
            dp.push_back(temp);
        }

        return dp.back();
    }
};