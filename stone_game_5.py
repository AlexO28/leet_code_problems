# There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
# In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
# The game ends when there is only one stone remaining. Alice's score is initially zero.
# Return the maximum score that Alice can obtain.
from typing import List
from itertools import accumulate
from functools import cache


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        self.stoneValue = stoneValue
        self.s = list(accumulate(stoneValue, initial=0))
        return self.search(0, len(stoneValue) - 1)

    @cache
    def search(self, i: int, j: int) -> int:
        if i >= j:
            return 0
        ans = 0
        l = 0
        r = self.s[j + 1] - self.s[i]
        for k in range(i, j):
            l += self.stoneValue[k]
            r -= self.stoneValue[k]
            if l < r:
                if ans >= l * 2:
                    continue
                ans = max(ans, l + self.search(i, k))
            elif l > r:
                if ans >= r * 2:
                    break
                ans = max(ans, r + self.search(k + 1, j))
            else:
                ans = max(ans, max(l + self.search(i, k), r + self.search(k + 1, j)))
        return ans
