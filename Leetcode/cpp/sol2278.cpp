
//https://leetcode.com/problems/percentage-of-letter-in-string/?submissionId=1637909404
class Solution {
public:
    int percentageLetter(string s, char letter) {
        int total_length = s.size();
        if(total_length == 0){
            return 0; // checks if the string  has elements
        }
        int n_ocurrences = count(s.begin(), s.end(), letter);
        int rslt = (double)n_ocurrences/total_length*100;
        return rslt;
    }
};