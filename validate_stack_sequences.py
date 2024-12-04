# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_index = 0
        stack = []
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return pop_index == len(pushed)
