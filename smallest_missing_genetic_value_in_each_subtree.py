# There is a family tree rooted at 0 consisting of n nodes numbered 0 to n - 1. You are given a 0-indexed integer array parents, where parents[i] is the parent for node i. Since node 0 is the root, parents[0] == -1.
# There are 105 genetic values, each represented by an integer in the inclusive range [1, 105]. You are given a 0-indexed integer array nums, where nums[i] is a distinct genetic value for node i.
# Return an array ans of length n where ans[i] is the smallest genetic value that is missing from the subtree rooted at node i.
# The subtree rooted at a node x contains node x and all of its descendant nodes.
from typing import List


class Solution:
    def smallestMissingValueSubtree(
        self, parents: List[int], nums: List[int]
    ) -> List[int]:
        ans = [1] * len(nums)
        self.nums = nums
        self.g = [[] for _ in range(len(nums))]
        idx = -1
        for i, p in enumerate(parents):
            if i:
                self.g[p].append(i)
            if self.nums[i] == 1:
                idx = i
        if idx == -1:
            return ans
        self.vis = [False] * len(nums)
        self.has = [False] * (len(nums) + 2)
        i = 2
        while idx != -1:
            self.search(idx)
            while self.has[i]:
                i += 1
            ans[idx] = i
            idx = parents[idx]
        return ans

    def search(self, i):
        if not self.vis[i]:
            self.vis[i] = True
            if self.nums[i] < len(self.has):
                self.has[self.nums[i]] = True
            for j in self.g[i]:
                self.search(j)
