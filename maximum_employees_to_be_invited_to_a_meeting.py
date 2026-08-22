# A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.
# The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.
# Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.
from typing import List
from collections import deque


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        return max(self.max_cycle(favorite), self.topological_sort(favorite))

    def max_cycle(self, favorite):
        vis = [False] * len(favorite)
        ans = 0
        for i in range(len(favorite)):
            if not vis[i]:
                cycle = []
                j = i
                while not vis[j]:
                    cycle.append(j)
                    vis[j] = True
                    j = favorite[j]
                for k, v in enumerate(cycle):
                    if v == j:
                        ans = max(ans, len(cycle) - k)
                        break
        return ans

    def topological_sort(self, favorite):
        indeg = [0] * len(favorite)
        dist = [1] * len(favorite)
        for v in favorite:
            indeg[v] += 1
        q = deque(i for i, v in enumerate(indeg) if v == 0)
        while q:
            i = q.popleft()
            dist[favorite[i]] = max(dist[favorite[i]], dist[i] + 1)
            indeg[favorite[i]] -= 1
            if indeg[favorite[i]] == 0:
                q.append(favorite[i])
        return sum(
            dist[i] for i, v in enumerate(favorite) if i == favorite[favorite[i]]
        )
