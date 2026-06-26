# You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.
# For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:
# You choose any number of obstacles between 0 and i inclusive.
# You must include the ith obstacle in the course.
# You must put the chosen obstacles in the same order as they appear in obstacles.
# Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
# Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.
from typing import List
from bisect import bisect_left


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        nums = sorted(set(obstacles))
        tree = BinaryIndexedTree(len(nums))
        ans = []
        for x in obstacles:
            i = bisect_left(nums, x) + 1
            ans.append(tree.query(i) + 1)
            tree.update(i, ans[-1])
        return ans


class BinaryIndexedTree:
    __slots__ = ["n", "c"]

    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, v):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x):
        s = 0
        while x:
            s = max(s, self.c[x])
            x -= x & -x
        return s
