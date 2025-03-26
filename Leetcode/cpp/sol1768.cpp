//https://leetcode.com/problems/merge-strings-alternately/solutions/6583176/100-time-by-antoniojsp-3re4/

class Solution {
public:
    string mergeAlternately(string word1, string word2) {

        string result = "";
        int i = 0, j = 0;
        while((i<word1.length()) || (j<word2.length()) ){

            if (i<word1.length()){
                result+=word1[i];
                i++;

            }
            if(j<word2.length()){
                result+=word2[j];
                j++;
            }
        }

        return result;

    }
};