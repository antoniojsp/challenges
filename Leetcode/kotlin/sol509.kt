
//https://leetcode.com/problems/fibonacci-number/

class Solution {
    fun fib(n: Int): Int {

        if(n == 0){
            return 0;
        }
        if(n == 1){
            return 1;
        }

        return fib(n-2)+fib(n-1);

    }
}