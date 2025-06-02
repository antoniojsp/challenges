

class Solution {
public:
    vector<int> prefix(vector<int> arr){
        vector<int> rslt = {1};
        for(int num:arr){
            rslt.push_back(rslt.back()*num);
        }
        return rslt;
    }

    vector<int> productExceptSelf(vector<int>& nums) {

        if (nums.size() <= 1){
            return nums;
        }

        vector<int> left_to_right = prefix(nums);
        reverse(nums.begin(), nums.end());
        vector<int> right_to_left = prefix(nums);
        reverse(right_to_left.begin(), right_to_left.end());
        vector<int> result(nums.size());
        for(int i = 0; i < result.size(); i++){
            result[i] = left_to_right[i]*right_to_left[i+1];
        }

        return result;
    }
};