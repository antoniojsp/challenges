class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {

        vector<int> trust_tracker(n, 0);
        vector<int> tracker(n, 0);
        for(auto person:trust){
            tracker[person[0]-1]--;
            tracker[person[1]-1]++;
        }
        for(int i = 0; i<tracker.size(); i++){
            if(tracker[i] == n-1){
                return i+1;
            }
        }
        return -1;
    }
};