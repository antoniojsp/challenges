
//https://leetcode.com/problems/intersection-of-two-arrays/submissions/1658507305/

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

        set<int> nums1_set(nums1.begin(), nums1.end());
        set<int> nums2_set(nums2.begin(), nums2.end());

        set<int> result;
        set_intersection(nums1_set.begin(), nums1_set.end(),
                        nums2_set.begin(), nums2_set.end(),
                        inserter(result, result.begin()));
        vector <int> rslt(result.begin(), result.end());

        return rslt;
    }
};