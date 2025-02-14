# Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.
# Implement the ProductOfNumbers class:
# ProductOfNumbers() Initializes the object with an empty stream.
# void add(int num) Appends the integer num to the stream.
# int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
# The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
class ProductOfNumbers:

    def __init__(self):
        self.num_dict = []
        

    def add(self, num: int) -> None:
        if num == 0:
            self.num_dict = []
        elif num == 1:
            self.num_dict.insert(0, 1)
        else:
            self.num_dict.insert(0, num)
            if len(self.num_dict) > 1:
                for j in range(1, len(self.num_dict)):
                    self.num_dict[j] *= num
                

    def getProduct(self, k: int) -> int:
        if k > len(self.num_dict):
            return 0
        else:
            return self.num_dict[k-1]
