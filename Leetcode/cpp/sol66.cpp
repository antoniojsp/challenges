
//https://leetcode.com/problems/plus-one/description/

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        for(int i = digits.size()-1; i >= 0; i--){
            if(digits[i]+1 <= 9){// digits[i]+1 less or equal than 9, then it fits in one index
                digits[i]++;
                return digits; // since it didn't carry a value, just add one and return
            }else{//if digits[i]+1 is greater than 9, it carries one to the next digit
                digits[i] = 0; // in the chance of digits[i] is 9, then it always turn to 10, since only adds one (ending in zero)
            }
        }
        vector<int> first_element = {1};
        vector<int> result = {1};
        result.insert(result.end(), digits.begin(), digits.end());
        return result;
    }
};