# You are given two integers memory1 and memory2 representing the available memory in bits on two memory sticks. There is currently a faulty program running that consumes an increasing amount of memory every second.
# At the ith second (starting from 1), i bits of memory are allocated to the stick with more available memory (or from the first memory stick if both have the same available memory). If neither stick has at least i bits of available memory, the program crashes.
# Return an array containing [crashTime, memory1crash, memory2crash], where crashTime is the time (in seconds) when the program crashed and memory1crash and memory2crash are the available bits of memory in the first and second sticks respectively.
from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        limit = 1
        num_iterations = 1
        while True:
            if memory1 >= memory2:
                diff = memory1 - limit
                if diff >= 0:
                    memory1 = diff
                else:
                    return [num_iterations, memory1, memory2]
            else:
                if memory2 >= memory1:
                    diff = memory2 - limit
                    if diff >= 0:
                        memory2 = diff
                    else:
                        return [num_iterations, memory1, memory2]
            num_iterations += 1
            limit += 1
