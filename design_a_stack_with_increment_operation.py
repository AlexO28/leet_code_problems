# Design a stack that supports increment operations on its elements.
# Implement the CustomStack class:
# CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
# void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
# int pop() Pops and returns the top of the stack or -1 if the stack is empty.
# void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize
        
    def push(self, x: int) -> None:
        if len(self.arr) < self.maxSize:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr.pop(len(self.arr)-1)

    def increment(self, k: int, val: int) -> None:
        if len(self.arr) > 0:
            for j in range(min(len(self.arr), k)):
                self.arr[j] += val
