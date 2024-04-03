# You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
​# Return the minimum number of intervals required to complete all tasks.
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        return max(len(tasks), (max_freq - 1) * (n + 1) + sum(freq == max_freq for freq in task_counts.values()))
