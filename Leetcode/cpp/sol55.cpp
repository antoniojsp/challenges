//https://leetcode.com/problems/min-stack/

class MinStack {

    vector <pair<int, int>> myStack;
    int minimum;

public:
    MinStack() {
        minimum = INT_MAX;
    }

    void push(int val) {
        // check first if the current minimum is greater that val
        if (val < minimum){
            minimum = val; // update minium
        }
        myStack.push_back({val, minimum});
    }

    void pop() {
        // no need to check if it's empty due problem's constraints
        myStack.pop_back();
        if (!myStack.empty()){
            int prev_min = myStack.back().second;
            minimum = prev_min;
        }else {
            minimum = INT_MAX;
        }

    }

    int top() {
        return myStack.back().first;
    }

    int getMin() {
        return minimum;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */