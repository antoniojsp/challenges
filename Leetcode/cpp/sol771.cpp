
// https://leetcode.com/problems/jewels-and-stones/

class Solution {
public:

    int numJewelsInStones(string jewels, string stones) {
        set<char> unique(jewels.begin(), jewels.end());
        int count = 0;
        for(auto i:stones){
            if(unique.contains(i)){
                count++;
            }
        }
        return count;
    }
};