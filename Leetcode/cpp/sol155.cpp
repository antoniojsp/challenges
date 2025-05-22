// https://leetcode.com/problems/min-stack/

struct currentAndValue{
    int current;
    int minimum;
};

class MinStack {
public:

    vector <currentAndValue> S;
    MinStack() {
    }

    void push(int val) {
        int minimum = val;
        if(!S.empty()){
            minimum = S.back().minimum;
        }
        currentAndValue new_value;
        new_value.current = val;
        new_value.minimum = minimum > val? val: minimum;
        S.push_back(new_value);
    }

    void pop() {
        S.pop_back();
    }

    int top() {
        return S.back().current;
    }

    int getMin() {
        return S.back().minimum;
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