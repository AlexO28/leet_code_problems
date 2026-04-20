# There is a donuts shop that bakes donuts in batches of batchSize. They have a rule where they must serve all of the donuts of a batch before serving any donuts of the next batch. You are given an integer batchSize and an integer array groups, where groups[i] denotes that there is a group of groups[i] customers that will visit the shop. Each customer will get exactly one donut.
# When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.
# You can freely rearrange the ordering of the groups. Return the maximum possible number of happy groups after rearranging the groups.
from typing import List
from functools import cache


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        self.g = [v % batchSize for v in groups if v % batchSize]
        self.mask = (1 << len(self.g)) - 1
        self.batchSize = batchSize
        return len(groups) - len(self.g) + self.search(0, 0)

    @cache
    def search(self, state, x):
        if state == self.mask:
            return 0
        vis = [False] * self.batchSize
        res = 0
        for i, v in enumerate(self.g):
            if state >> i & 1 == 0 and not vis[v]:
                vis[v] = True
                y = (x + v) % self.batchSize
                res = max(res, self.search(state | 1 << i, y))
        return res + (x == 0)
