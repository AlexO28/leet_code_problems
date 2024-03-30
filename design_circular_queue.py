class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.arr) == self.size:
            return False
        else:
            self.arr.append(value)
            return True

    def deQueue(self) -> bool:
        if len(self.arr) == 0:
            return False
        else:
            if len(self.arr) == 1:
                self.arr = []
            else:
                self.arr = self.arr[1:]
            return True

    def Front(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[0]

    def Rear(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]
        
    def isEmpty(self) -> bool:
        return len(self.arr) == 0

    def isFull(self) -> bool:
        return len(self.arr) == self.size        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
