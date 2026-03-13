
//https://leetcode.com/problems/min-stack/description/

class MinStack {
    stack:[number,number][];
    constructor() {
        this.stack = [];
    }

    push(val: number): void {
        if(this.stack.length == 0){
            this.stack.push([val, val]);
        }else{
            const min = this.getMin();
            if(min <= val){
                this.stack.push([val, min]);
            }else{
                this.stack.push([val, val]);
            }
        }
    }

    pop(): void {
        if(this.stack.length > 0){
            this.stack.pop();
        }
    }

    top(): number {
        return this.stack.at(-1)[0];
    }

    getMin(): number {
        return this.stack.at(-1)[1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */