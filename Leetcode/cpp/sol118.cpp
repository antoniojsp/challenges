
// https://leetcode.com/problems/pascals-triangle/description/
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if(numRows == 1){
            return {{1}};
        }
        vector<vector<int>> result = generate(numRows - 1);
        vector<int> prev = result.back();
        vector<int> new_row = {1};
        for(int i = 1; i < prev.size(); i++){
            new_row.push_back(prev[i]+prev[i-1]);
        }
        new_row.push_back(1);
        result.push_back(new_row);
        return result;
    }
};