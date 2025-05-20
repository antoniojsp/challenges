//https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution {
public:

    pair<int, double> coordinates(int pos, int width) {
        return make_pair(pos/width, pos%width);
    }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int start = 0;
        int end = matrix.size()*matrix[0].size()-1;
        while(start<=end){
            int mid = (start+end)/2;
            auto [x, y] = coordinates(mid, matrix[0].size());
            if(matrix[x][y] == target){
                return true;
            }else if(matrix[x][y] > target){
                end = mid - 1;
            }else{
                start = start +1;
            }
        }

        return false;

    }
};