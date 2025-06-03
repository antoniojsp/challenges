
// https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
class KthLargest {
public:
    priority_queue<int, std::vector<int>, std::greater<int>> minIntHeap;
    int kth;
    KthLargest(int k, vector<int>& nums) {
        for(int num:nums){
            minIntHeap.push(num);
        }
        kth = k;
        check_size();
    }

    void check_size(){
        while (minIntHeap.size() > kth){
             minIntHeap.pop();
        }
    }

    int add(int val) {
        minIntHeap.push(val);
        check_size();
        return minIntHeap.top();

    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */