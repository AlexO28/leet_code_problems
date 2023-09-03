# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

from collections import deque


class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dictCourses = {}
        nums = [0] * numCourses
        for a, b in prerequisites:
            if b in dictCourses.keys():
                dictCourses[b].append(a)
            else:
                dictCourses[b] = [a]
            nums[a] += 1
        queue = deque([i for i, v in enumerate(nums) if v == 0])
        ans = []
        while queue:
            i = queue.popleft()
            ans.append(i)
            if i in dictCourses.keys():
                for j in dictCourses[i]:
                    nums[j] -= 1
                    if nums[j] == 0:
                        queue.append(j)
        return ans if len(ans) == numCourses else []
