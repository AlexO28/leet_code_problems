# A Bitset is a data structure that compactly stores bits.
# Implement the Bitset class:
# Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
# void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.
# void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.
# void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.
# boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
# boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
# int count() Returns the total number of bits in the Bitset which have value 1.
# String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.
class Bitset:

    def __init__(self, size: int):
        self.string = ["0"] * size
        self.zeros = set([i for i in range(size)])
        self.ones = set()

    def fix(self, idx: int) -> None:
        self.ones.add(idx)
        self.zeros.discard(idx)

    def unfix(self, idx: int) -> None:
        self.zeros.add(idx)
        self.ones.discard(idx)
        
    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones

    def all(self) -> bool:
        return len(self.zeros) == 0

    def one(self) -> bool:
        return len(self.ones) > 0
        
    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        for i in self.zeros:
            self.string[i] = "0"
        for i in self.ones:
            self.string[i] = "1"
        return "".join(self.string)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
