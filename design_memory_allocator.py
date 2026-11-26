# You are given an integer n representing the size of a 0-indexed memory array. All memory units are initially free.
# You have a memory allocator with the following functionalities:
# Allocate a block of size consecutive free memory units and assign it the id mID.
# Free all memory units with the given id mID.
# Note that:
# Multiple blocks can be allocated to the same mID.
# You should free all the memory units with mID, even if they were allocated in different blocks.
# Implement the Allocator class:
# Allocator(int n) Initializes an Allocator object with a memory array of size n.
# int allocate(int size, int mID) Find the leftmost block of size consecutive free memory units and allocate it with the id mID. Return the block's first index. If such a block does not exist, return -1.
# int freeMemory(int mID) Free all memory units with the id mID. Return the number of memory units you have freed.
class Allocator:

    def __init__(self, n: int):
        self.nums = [0] *  n


    def allocate(self, size: int, mID: int) -> int:
        prev_zero_index = -1
        cur_strike = 0
        for j in range(len(self.nums)):
            if self.nums[j] > 0:
                prev_zero_index = -1
                cur_strike = 0
            else:
                cur_strike += 1
                if prev_zero_index < 0:
                    prev_zero_index = j
                if cur_strike == size:
                    break
        else:
            return -1
        for j in range(prev_zero_index, prev_zero_index + size, 1):
            self.nums[j] = mID
        return prev_zero_index

    def freeMemory(self, mID: int) -> int:
        count = 0
        for j in range(len(self.nums)):
            if self.nums[j] == mID:
                count += 1
                self.nums[j] = 0
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
