# You are given an array tasks where tasks[i] = [actuali, minimumi]:
# actuali is the actual amount of energy you spend to finish the ith task.
# minimumi is the minimum amount of energy you require to begin the ith task.
# For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.
# You can finish the tasks in any order you like.
# Return the minimum initial amount of energy you will need to finish all the tasks.
from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        ans = 0
        cur = 0
        tasks = sorted(tasks, key=lambda x: x[0] - x[1])
        for a, m in tasks:
            delta = m - cur
            if delta > 0:
                ans += delta
                cur = m
            cur -= a
        return ans
