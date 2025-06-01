
//https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_map = {{0,1}};
        int prefix_sum = 0;
        int count = 0;
        for(int num:nums){
            prefix_sum+=num; //add the current sum of the array
            int needed = prefix_sum - k; // find a previous sum in the array so substracting would get us k
            if(prefix_map.count(needed)){
                count+=prefix_map[needed];
            }
            prefix_map[prefix_sum]+=1;
        }

        return count;

    }
};

