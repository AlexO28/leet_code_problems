# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        dp_table = [[float("inf")] * (d + 1) for i in range(len(jobDifficulty) + 1)]
        dp_table[0][0] = 0
        for i in range(1, len(jobDifficulty) + 1):
            for j in range(1, min(d + 1, i + 1)):
                max_difficulty_on_last_day = 0
                for k in range(i, 0, -1):
                    max_difficulty_on_last_day = max(
                        max_difficulty_on_last_day, jobDifficulty[k - 1]
                    )
                    dp_table[i][j] = min(
                        dp_table[i][j],
                        dp_table[k - 1][j - 1] + max_difficulty_on_last_day,
                    )
        if dp_table[len(jobDifficulty)][d] == float("inf"):
            return -1
        else:
            return dp_table[len(jobDifficulty)][d]
