# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

from collections import deque


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursesDict = {}
        nums = [0]*numCourses
        for prerequisite in prerequisites:
            if prerequisite[1] in coursesDict.keys():
                coursesDict[prerequisite[1]].append(prerequisite[0])
            else:
                coursesDict[prerequisite[1]] = [prerequisite[0]]
            nums[prerequisite[0]] += 1
        counter = 0
        queue = deque([i for i, v in enumerate(nums) if v == 0])
        while queue:
            i = queue.popleft()
            counter += 1
            if counter > numCourses:
                return False
            if i in coursesDict.keys():
                for j in coursesDict[i]:
                    nums[j] -= 1
                    if nums[j] == 0:
                        queue.append(j)
        return counter == numCourses
