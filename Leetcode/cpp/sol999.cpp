// https://leetcode.com/problems/available-captures-for-rook/

class Solution {
public:
    pair<int, int> find_rook(vector<vector<char>>& board){
        int row, col = 0;
        for(int i = 0; i<board.size(); i++){
            for(int j = 0; j<board[0].size(); j++){
                if(board[i][j] == 'R'){
                    row = i;
                    col = j;
                }
            }
        }
        return {row, col};
    }

    int numRookCaptures(vector<vector<char>>& board) {
        pair<int, int> pos = find_rook(board);
        vector<pair<int, int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};
        int count  = 0;
        for(auto dir: directions){
            int row = dir.first + pos.first;
            int col = dir.second + pos.second;
            while(row < 8 && 0 <= row && col < 8 && 0 <= col){
                if(board[row][col] == 'p'){
                    count++;
                    break;
                }
                if(board[row][col] == 'B'){
                    break;
                }
                row+= dir.first;
                col+= dir.second;
            }

        }
        return count;
    }
};