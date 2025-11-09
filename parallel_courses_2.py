# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei. Also, you are given the integer k.
# In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semesters for the courses you are taking.
# Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is possible to take every course.
from collections import deque
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        prerequisites = [0] * (n + 1)
        for prereq, course in relations:
            prerequisites[course] |= 1 << prereq
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            completed_courses, semester_count = queue.popleft()
            if completed_courses == (1 << (n + 1)) - 2:
                return semester_count
            available_courses = 0
            for course_id in range(1, n + 1):
                if (completed_courses & prerequisites[course_id]) == prerequisites[
                    course_id
                ]:
                    available_courses |= 1 << course_id
            available_courses ^= completed_courses
            if available_courses.bit_count() <= k:
                new_state = available_courses | completed_courses
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, semester_count + 1))
            else:
                subset = available_courses
                while subset:
                    if subset.bit_count() == k:
                        new_state = subset | completed_courses
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, semester_count + 1))
                    subset = (subset - 1) & available_courses
