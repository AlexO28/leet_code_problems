# There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.
# You will start on the 1st day and you cannot take two or more courses simultaneously.
# Return the maximum number of courses that you can take.
from heapq import heappush, heappop


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        max_heap = []      
        total_duration = 0      
        for duration, last_day in courses:
            heappush(max_heap, -duration)
            total_duration += duration          
            while total_duration > last_day:
                total_duration += heappop(max_heap)
        return len(max_heap)
