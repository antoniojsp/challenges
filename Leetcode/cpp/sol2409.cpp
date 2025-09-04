
// https://leetcode.com/problems/count-days-spent-together/description/

class Solution {
public:
    int ith_day(string date){
        vector <int> months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        string month = date.substr(0, 2);
        string day = date.substr(3, 2);
        int m = stoi(month);
        int d = stoi(day);
        int days = 0;
        for(int i = 0; i<m-1; i++){
            days+=months[i];
        }
        return days + d;
    }

    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int alice_a = ith_day(arriveAlice);
        int alice_l = ith_day(leaveAlice);
        int bob_a = ith_day(arriveBob);
        int bob_l = ith_day(leaveBob);

        int start = max(alice_a, bob_a);
        int end = min(alice_l, bob_l);
        return max(0, end - start+1);

    }
};