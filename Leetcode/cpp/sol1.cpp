
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

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /*Using a hashmap, check every value in "nums" and check
        if you have seen the that what you need to reach the target sum
        wtih your current value*/
        unordered_map<int, int> seen; // hashmap
        for (int i = 0;i<nums.size(); i++){
            auto complement = target - nums[i]; // get how much you need to add to the current value to reach the target
            if (seen.find(complement) != seen.end()){ // if you have already seen the complement, just return
                return {i, seen[complement]};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};