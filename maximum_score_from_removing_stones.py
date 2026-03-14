# You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).
# Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score = 0
        piles = [a, b, c]
        while True:
            min_val = min(piles)
            index = piles.index(min_val)
            crit_val = 0
            for j in range(len(piles)):
                if j != index:
                    piles[j] -= 1
                    crit_val = min(crit_val, piles[j])
            if crit_val == 0:
                score += 1
            else:
                break
        return score
