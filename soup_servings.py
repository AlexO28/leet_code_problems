# There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:
# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B, and
# Serve 25 ml of soup A and 75 ml of soup B.
# When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.
# Note that we do not have an operation where all 100 ml's of soup B are used first.
# Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.
from functools import cache
import numpy as np

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        n = int(np.ceil(n/25))
        return self.serve(n, n)

    @cache
    def serve(self, a, b):
        if (a <= 0) and (b <= 0):
            return 0.5
        elif a <= 0:
            return 1
        elif b <= 0:
            return 0
        else:
            return 0.25*(self.serve(a-4, b) + self.serve(a-3, b-1) + self.serve(a-2, b-2) + self.serve(a-1, b-3))
