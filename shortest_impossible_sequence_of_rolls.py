# You are given an integer array rolls of length n and an integer k. You roll a k sided dice numbered from 1 to k, n times, where the result of the ith roll is rolls[i].
# Return the length of the shortest sequence of rolls so that there's no such subsequence in rolls.
# A sequence of rolls of length len is the result of rolling a k sided dice len times.
class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        res = 1
        s = set()
        for v in rolls:
            s.add(v)
            if len(s) == k:
                res += 1
                s.clear()
        return res
