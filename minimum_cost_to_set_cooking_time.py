# A generic microwave supports cooking times for:
# at least 1 second.
# at most 99 minutes and 99 seconds.
# To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,
# You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.
# There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.
# Return the minimum cost to set targetSeconds seconds of cooking time
# Remember that one minute consists of 60 seconds.
from math import inf


class Solution:
    def minCostSetTime(
        self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int
    ) -> int:
        m, s = divmod(targetSeconds, 60)
        return min(
            self.cost(m, s, startAt, moveCost, pushCost),
            self.cost(m - 1, s + 60, startAt, moveCost, pushCost),
        )

    def cost(self, m, s, startAt, moveCost, pushCost):
        if not 0 <= m < 100 or not 0 <= s < 100:
            return inf
        arr = [m // 10, m % 10, s // 10, s % 10]
        i = 0
        while i < 4 and arr[i] == 0:
            i += 1
        t = 0
        prev = startAt
        for v in arr[i:]:
            if v != prev:
                t += moveCost
            t += pushCost
            prev = v
        return t
