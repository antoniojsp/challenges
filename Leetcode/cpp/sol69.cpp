// https://leetcode.com/problems/sqrtx/description/


class Solution {
public:
    int mySqrt(int x) {
        int left = 0;
        int right = x;
        while (left <= right){
            long long mid = (int)((left+right)/2);
            long long square = mid*mid;
            if(square == x){
                return mid;
            }else if (square > x){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }

        return right;
    }
};