class Solution {
public:

    int even_val(vector<int>& nums){
        int count = 0;
        for(int i: nums){
            if (i%2 ==0){
                count++;
            }
        }
        return count;
    }

    vector<int> transformArray(vector<int>& nums) {

        int even_count = even_val(nums);
        int odd_count = nums.size() - even_count;

        vector<int> results(even_count, 0);
        results.insert(results.end(),odd_count, 1);


        return results;
    }
};