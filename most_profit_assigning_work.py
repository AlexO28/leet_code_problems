# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.
# For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.
import numpy as np


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(reverse=True)
        arrinds = np.argsort(difficulty)
        difficulty = np.array(difficulty)[arrinds]
        profit = np.array(profit)[arrinds]
        maxprofit = []
        curmax = -1
        for j in range(len(profit)):
            curmax = max(curmax, profit[j])
            maxprofit.append(curmax)
        worker_num = 0
        profit_sum = 0
        j = len(difficulty) - 1
        while (j >= 0) and (worker_num < len(worker)):
            if difficulty[j] <= worker[worker_num]:
                profit_sum += maxprofit[j]
                worker_num += 1
            else:
                j -= 1
        return profit_sum
