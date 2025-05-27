//https://leetcode.com/problems/count-integers-with-even-digit-sum/description/

class Solution {
public:

    int sum_digits(int num){
        int sum = 0;
        while (0 < num){
            sum+=num%10;
            num/=10;
        }
        return sum;
    }
    int countEven(int num) {
        int count = 0;
        for(int i = 2; i<=num; i++){
            if (sum_digits(i)%2 == 0){
                count++;
            }
        }

        return count;
    }
};