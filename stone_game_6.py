# Alice and Bob take turns playing a game, with Alice starting first.
# There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.
# You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.
# The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.
# Determine the result of the game, and:
# If Alice wins, return 1.
# If Bob wins, return -1.
# If the game results in a draw, return 0.
from typing import List
import numpy as np


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        aliceValues = np.array(aliceValues)
        bobValues = np.array(bobValues)
        totalValues = [aliceValues[j] + bobValues[j] for j in range(len(aliceValues))]
        indices = np.lexsort((aliceValues, totalValues))[::-1]
        aliceValues = aliceValues[indices]
        bobValues = bobValues[indices]
        aliceScore = 0
        bobScore = 0
        for j in range(len(totalValues)):
            if j % 2 == 0:
                aliceScore += aliceValues[j]
            else:
                bobScore += bobValues[j]
        if aliceScore > bobScore:
            return 1
        elif aliceScore < bobScore:
            return -1
        else:
            return 0
