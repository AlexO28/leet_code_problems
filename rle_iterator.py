# We can use run-length encoding (i.e., RLE) to encode a sequence of integers. In a run-length encoded array of even length encoding (0-indexed), for all even i, encoding[i] tells us the number of times that the non-negative integer value encoding[i + 1] is repeated in the sequence.
# For example, the sequence arr = [8,8,8,5,5] can be encoded to be encoding = [3,8,2,5]. encoding = [3,8,0,9,2,5] and encoding = [2,8,1,8,2,5] are also valid RLE of arr.
# Given a run-length encoded array, design an iterator that iterates through it.
# Implement the RLEIterator class:
# RLEIterator(int[] encoded) Initializes the object with the encoded array encoded.
# int next(int n) Exhausts the next n elements and returns the last element exhausted in this way. If there is no element left to exhaust, return -1 instead.
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.pos = 0
        

    def next(self, n: int) -> int:
        if self.pos == len(self.encoding):
            return -1
        while n > 0:
            while self.encoding[self.pos] == 0:
                self.pos += 2
                if self.pos >= len(self.encoding):
                    self.pos = len(self.encoding)
                    return -1
            if n > self.encoding[self.pos]:
                n -= self.encoding[self.pos]
                self.encoding[self.pos] = 0
            else:
                self.encoding[self.pos] -= n
                n = 0
                return self.encoding[self.pos + 1]
