class Solution {
public:
    int countAsterisks(string s) {

        bool flag = false;
        int count = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] == '*' && flag == false){
                count++;
            }
            if(s[i] == '|'){
                flag = !flag;
            }
        }

        return  count;
    }
};