class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) > 0:
            elem = self.arr[-1]
            if len(self.arr) > 1:
                self.arr = self.arr[:(len(self.arr)-1)]
            else:
                self.arr = []
            return elem

    def top(self) -> int:
        if len(self.arr) > 0:
            return self.arr[-1]

    def empty(self) -> bool:
        return len(self.arr) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
