# You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
# There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
# Return the minimum possible maximum working time of any assignment.
from typing import List
from math import inf


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.k = k
        self.jobs = jobs
        self.cnt = [0] * k
        self.jobs.sort(reverse=True)
        self.ans = inf
        self.dfs(0)
        return self.ans

    def dfs(self, i):
        if i == len(self.jobs):
            self.ans = min(self.ans, max(self.cnt))
            return
        for j in range(self.k):
            if self.cnt[j] + self.jobs[i] >= self.ans:
                continue
            self.cnt[j] += self.jobs[i]
            self.dfs(i + 1)
            self.cnt[j] -= self.jobs[i]
            if self.cnt[j] == 0:
                break
