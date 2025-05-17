# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.
# Implement the DinnerPlates class:
# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
# void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
# int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
# int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.
from sortedcontainers import SortedSet


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.partially_full = SortedSet() 


    def push(self, val: int) -> None:
        if not self.partially_full:
            self.stacks.append([val])
            if self.capacity > 1:
                self.partially_full.add(len(self.stacks) - 1)
        else:
            index = self.partially_full[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.capacity:
                self.partially_full.discard(index)        


    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)
        

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if index == len(self.stacks) - 1 and not self.stacks[-1]:
            while self.stacks and not self.stacks[-1]:
                self.partially_full.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            self.partially_full.add(index)
        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
