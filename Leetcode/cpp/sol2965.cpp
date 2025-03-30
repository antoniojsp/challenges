#include <cmath>
class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {

        map<int,int> freq;
        for (auto i = 1; i<=pow(grid.size(), 2); i++){
            freq[i] = 0;
        }
        for(auto row:grid){
            for (int j:row){
                freq[j]++;
            }
        }

        vector <int> results({0,0});

        for (auto i = freq.begin(); i != freq.end();i++){
            if(i->second == 0){
                results[1] = i->first;
            }else if(i->second == 2){
                results[0] = i->first;

            }
        }
        return results;
    }
};