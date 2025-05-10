
//https://leetcode.com/problems/two-sum/submissions/1630104969/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        map<int, int> seen;
        for(int i = 0; i < nums.size(); i++){
            int remainder = target - nums[i];
            if (seen.count(remainder) > 0){
                return {i, seen[remainder]};
            }else{
                seen[nums[i]] = i;
            }
        }
        return {};
    }
};