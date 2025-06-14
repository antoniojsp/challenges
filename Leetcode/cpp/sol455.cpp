
// https://leetcode.com/problems/assign-cookies/

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int children = 0, cookies = 0;

        while(children < g.size() && cookies < s.size()){
            if(s[cookies]>=g[children]){
                children++;
            }
            cookies++;
        }

        return children;
    }
};