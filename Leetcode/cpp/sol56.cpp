
// https://leetcode.com/problems/merge-intervals/description/
class Solution {
public:
    static bool sorting(const vector<int>& a, const vector<int>& b){
        return a[0] < b[0];
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.empty()){ // if empty, return empty vector (constraints indicate that all intervals are at least one range, but just in case)
            return {};
        }
        sort(intervals.begin(), intervals.end(), sorting);
        vector<vector<int>> result = {intervals[0]};
        for (int i = 1; i < intervals.size(); i++){
            int start = result.back()[0], end = result.back()[1];
            int start_n = intervals[i][0], end_n = intervals[i][1];

            if(end  >= start_n){ // end in last range in results is greater than the start range from the current range, then indicate that is interlaping and needs to be fusion
                result.back()[1] = max(end, end_n);
            }else{
                result.push_back(intervals[i]);
            }
        }

        return result;
    }
};
