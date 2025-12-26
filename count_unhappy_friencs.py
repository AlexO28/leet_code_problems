# You are given a list of preferences for n friends, where n is always even.
# For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.
# All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.
# However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:
# x prefers u over y, and
# u prefers x over v.
# Return the number of unhappy friends.
from typing import List


class Solution:
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        d = [{x: j for j, x in enumerate(p)} for p in preferences]
        p = {}
        for x, y in pairs:
            p[x] = y
            p[y] = x
        ans = 0
        for x in range(n):
            y = p[x]
            for i in range(d[x][y]):
                u = preferences[x][i]
                v = p[u]
                if d[u][x] < d[u][v]:
                    ans += 1
                    break
        return ans
