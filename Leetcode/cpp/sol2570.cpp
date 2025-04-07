
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

#include <algorithm> // For std::copy and std::move (C++11 and later) b

class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {

        map<int,int> seen;
        for(auto i : nums2){
            nums1.push_back(i);
        }
        for (auto i: nums1){
            if(seen.find(i[0]) == seen.end()){
                seen[i[0]] = 0;
            }
            seen[i[0]] += i[1];
        }
        vector <vector<int>> result;
        for(auto i: seen){
            result.push_back({i.first, i.second});
        }

        return result;
    }
};