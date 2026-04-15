# You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.
# Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
# Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.
# Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.
from typing import List
from math import inf


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        min_dist = inf
        delta = 0
        next_ind_right = startIndex
        next_ind_left = startIndex
        while delta < len(words) - 1:
            delta += 1
            next_ind_right = (next_ind_right + 1) % len(words)
            if words[next_ind_right] == target:
                return delta
            next_ind_left = (next_ind_left - 1) % len(words)
            if words[next_ind_left] == target:
                return delta
        return -1
