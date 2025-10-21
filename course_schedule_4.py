# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
# Return a boolean array answer, where answer[j] is the answer to the jth query.
from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        for prereq, course in prerequisites:
            is_prerequisite[prereq][course] = True
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True
        return [is_prerequisite[prereq][course] for prereq, course in queries]
