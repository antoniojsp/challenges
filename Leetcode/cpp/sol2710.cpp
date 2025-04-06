
#  https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
public:
    string removeTrailingZeros(string num) {

        int ending = 0;
        for (int i = num.size() - 1 ; num[i] == '0'; --i)
            ending++;

        return num.substr(0, num.size()-ending);
    }
};