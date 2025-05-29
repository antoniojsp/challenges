// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution {
public:
    void print(vector<int> arr){
        for(auto i:arr){
            cout << i << " ";
        }
        cout << endl;
    }
    int oddCells(int m, int n, vector<vector<int>>& indices) {

        vector<int> row(m, 0);
        vector<int> col(n, 0);
        for (auto i:indices){
            row[i[0]]++;
            col[i[1]]++;
        }
        int result = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if ((row[i] + col[j]) % 2 != 0){
                    result++;
                }
            }
        }

        return result;
    }
};