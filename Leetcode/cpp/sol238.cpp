

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



class Solution {
public:
    void print(vector<int> arr){
        for(int i: arr){
            cout << i << " ";
        }
        cout << endl;
    }

    vector<int> productExceptSelf(vector<int>& nums) {
        if (nums.size() <= 1){
            return nums;
        }
        vector<int> result(nums.size(), 1);
        for (int i = 1; i < nums.size(); ++i) { // calculate for the left
            result[i] = result[i - 1] * nums[i - 1];
        }

        int from_the_right = 1;
        for(int i = nums.size()-1; 0 <= i; i--){ // now calculate from the right.
            result[i] *= from_the_right;
            from_the_right *= nums[i];
        }
        return result;
    }
};
