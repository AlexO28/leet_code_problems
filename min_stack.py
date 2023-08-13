# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

class MinStack:

    def __init__(self):
        self.stack = []
        self.pal = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.pal.keys():
            self.pal[val].append(len(self.stack) - 1)
        else:
            self.pal[val] = [len(self.stack) - 1]

    def pop(self) -> None:
        if len(self.stack) > 0:
            elem = self.stack.pop(-1)
            self.pal[elem].pop(-1)
            if len(self.pal[elem]) == 0:
                self.pal.pop(elem, None)

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        min_indices = self.pal[min(self.pal.keys())]
        return self.stack[min_indices[0]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin(
