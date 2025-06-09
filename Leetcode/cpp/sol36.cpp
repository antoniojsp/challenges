
// https://leetcode.com/problems/valid-sudoku/description/


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        map<int, set<char>> row;
        map<int, set<char>> column;
        map<pair<int,int>, set<char>> boxes;
        int length = 9;

        for (int i = 0; i < length; i++){
            for (int j = 0; j < length; j++){
                char current = board[i][j];
                if (current == '.'){
                    continue;
                }

                if (row[i].count(current)){
                    return false;
                }

                if (column[j].count(current)){
                    return false;
                }

                int r = i/3;
                int c = j/3;

                pair<int,int> box = {r,c};
                if(boxes[box].count(current)){
                    return false;
                }

                row[i].insert(current);
                column[j].insert(current);
                boxes[box].insert(current);

            }
        }


        return true;
    }
};