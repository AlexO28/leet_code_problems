# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq_dict = Counter(tasks)
        number_of_rounds = 0
        for freq in freq_dict.values():
            if freq == 1:
                return -1
            elif freq == 4:
                number_of_rounds += 2
            else:
                main_part, remainder = divmod(freq, 3)
                if remainder == 0:
                    number_of_rounds += main_part
                elif remainder == 2:
                    number_of_rounds += main_part + 1
                else:
                    main_part, remainder = divmod(freq - 2, 3)
                    number_of_rounds += main_part + 2
        return number_of_rounds
