class Solution {
public:

    void printv(vector<int>& temp){
        for(auto i:temp){
            cout << i <<" ";
        }
    }

    vector<int> getSneakyNumbers(vector<int>& nums) {
        auto max_value = max_element(nums.begin(), nums.end());
        vector<int>result(*max_value+1, 0);
        for (auto i: nums){
            result[i]++;
        }
        vector<int> resultado;
        for (auto i = 0; i<result.size();i++){
            if(result[i]==2){
                resultado.push_back(i);
            }
        }

        return resultado;
    }
};