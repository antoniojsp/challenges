// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<int> seen;
        int l = 0;
        int max_count = 0;
        for (int i = 0; i < s.size(); i++){
            while(seen.count(s[i])){
                seen.erase(s[l]);
                l++;
            }
            seen.insert(s[i]);
            int current = i - l+1;
            cout << current << endl;
            // max_count = max_count ? max_count < current: current;
            max_count = max(max_count, current);
        }
        return max_count;
    }
};
