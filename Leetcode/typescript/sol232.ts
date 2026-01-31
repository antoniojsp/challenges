
// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    private stack1:number[] = [];
    private stack2:number[] = [];
    private length:number = 0;
    push(x: number): void {
        this.stack1.push(x);
        this.length++;
    }

    transfer():void{
        if(this.stack2.length == 0){
            while(0 < this.stack1.length){
                this.stack2.push(this.stack1.pop());
            }
        }
    }
    pop(): number {
        if(this.empty()){
            return -1;
        }
        this.transfer();
        this.length--;
        return this.stack2.pop();
    }
    peek(): number {
        if(this.empty()){
            return -1;
        }
        this.transfer();
        return this.stack2.at(-1);
    }
    empty(): boolean {
        return this.length == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */


