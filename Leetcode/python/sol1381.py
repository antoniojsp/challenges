# https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.stack.append(x)
            self.siz e+ =1

    def pop(self) -> int:
        rslt = -1
        if self.size == 0:
            return rslt
        self.siz e- =1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:

        if k > self.size:
            for i in range(0, self.size):
                self.stack[i ]+ =val
        else:
            for i in range(0, k):
                self.stack[i ]+ =val


            # Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)