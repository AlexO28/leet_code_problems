# You are given two identical eggs and you have access to a building with n floors labeled from 1 to n.
# You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
# In each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.
from math import inf


class Solution:
    def twoEggDrop(self, n: int) -> int:
        f = [0] + [inf] * n
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                f[i] = min(f[i], 1 + max(j - 1, f[i - j]))
        return f[-1]
