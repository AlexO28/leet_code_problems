# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
# You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
import random
import bisect

class Solution:

    def __init__(self, w: List[int]):
        summa = 0
        self.weights = []
        for weight in w:
            summa += weight
            self.weights.append(summa)

    def pickIndex(self) -> int:
        ind = bisect.bisect_left(self.weights, random.randint(1, self.weights[-1]))
        return ind
