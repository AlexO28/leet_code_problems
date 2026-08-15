# You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.
# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.
# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.
# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
from typing import List
from collections import defaultdict, deque


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        vis = [False] * n
        vis[0] = vis[firstPerson] = True
        meetings.sort(key=lambda x: x[2])
        i = 0
        m = len(meetings)
        while i < m:
            j = i
            while (j + 1 < m) and (meetings[j + 1][2] == meetings[i][2]):
                j += 1
            s = set()
            g = defaultdict(list)
            for x, y, _ in meetings[i : j + 1]:
                g[x].append(y)
                g[y].append(x)
                s.update([x, y])
            q = deque([u for u in s if vis[u]])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        q.append(v)
            i = j + 1
        return [i for i, v in enumerate(vis) if v]
