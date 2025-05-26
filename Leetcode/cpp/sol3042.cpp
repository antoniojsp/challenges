
//https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

 class Solution {
public:

    bool isPrefixAndSuffix(const string &str1, const string &str2){
        if (str1.size() > str2.size()){
            return false;
        }
        int size1 = str1.size();
        int size2 = str2.size();
        for(int i = 0; i<size1; i++){
            if (str1[size1-1-i] != str2[size2-1-i] || str1[i] != str2[i]){
                return false;
            }
        }
        return true;
    }

    int countPrefixSuffixPairs(vector<string>& words) {
        int rslt = 0;
        for(int i = 0; i<words.size(); i++){
            for(int j = i + 1; j<words.size(); j++){
                if(isPrefixAndSuffix(words[i], words[j])){
                    rslt++;
                }
            }
        }
        return rslt;
    }
};