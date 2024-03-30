# Design your implementation of the circular double-ended queue (deque).
# Implement the MyCircularDeque class:
# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.arr = []

    def insertFront(self, value: int) -> bool:
        if len(self.arr) == self.size:
            return False
        else:
            self.arr.insert(0, value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.arr) == self.size:
            return False
        else:
            self.arr.append(value)
            return True
        

    def deleteFront(self) -> bool:
        if len(self.arr) == 0:
            return False
        else:
            if len(self.arr) == 1:
                self.arr = []
            else:
                self.arr = self.arr[1:]
            return True
 
    def deleteLast(self) -> bool:
        if len(self.arr) == 0:
            return False
        else:
            if len(self.arr) == 1:
                self.arr = []
            else:
                self.arr = self.arr[:(len(self.arr)-1)]
            return True        

    def getFront(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[0]

    def getRear(self) -> int:
        if len(self.arr) == 0:
            return -1
        else:
            return self.arr[-1]

    def isEmpty(self) -> bool:
        return (len(self.arr) == 0)
        

    def isFull(self) -> bool:
        return (len(self.arr) == self.size)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
