//https://leetcode.com/problems/alternating-digit-sum/description/
class Solution {
public:
    int alternateDigitSum(int n) {

        vector <int> stack;
        while (1 <= n){
            int temp = n%10;
            n/=10;
            stack.push_back(temp);
        }

        int result = 0;
        int base = 1;
        while (!stack.empty()){
            int val = stack.back();
            stack.pop_back();
            result+= base*val;
            base*=-1;
        }

        return result;
    }
};