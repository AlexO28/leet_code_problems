class MyQueue:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) == 0:
            return None
        elem = self.arr.pop(0)
        return elem
        
    def peek(self) -> int:
        if len(self.arr) == 0:
            return None
        return self.arr[0]

    def empty(self) -> bool:
        return len(self.arr) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
