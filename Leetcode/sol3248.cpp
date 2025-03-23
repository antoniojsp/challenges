class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {

        int x = 0, y = 0;

        for (string i: commands){
            if(i == "DOWN"){
                x++;
            }else if(i == "UP"){
                x--;
            }else if(i == "LEFT"){
                y--;
            }else{
                y++;
            }
        }

        return n*x+y;
    }
};