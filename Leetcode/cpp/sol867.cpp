//https://leetcode.com/problems/transpose-matrix/description/

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        vector <vector<int>> result;
        for(auto col = 0; col <matrix[0].size(); col++){
            vector<int> temp = {};
            for(auto row = 0; row<matrix.size(); row++){
                temp.push_back(matrix[row][col]);
            }
            result.push_back(temp);
        }

        return result;

    }
};