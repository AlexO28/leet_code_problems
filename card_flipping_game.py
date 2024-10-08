# You are given two 0-indexed integer arrays fronts and backs of length n, where the ith card has the positive integer fronts[i] printed on the front and backs[i] printed on the back. Initially, each card is placed on a table such that the front number is facing up and the other is facing down. You may flip over any number of cards (possibly zero).
# After flipping the cards, an integer is considered good if it is facing down on some card and not facing up on any card.
# Return the minimum possible good integer after flipping the cards. If there are no good integers, return 0.
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        prohibited = list(set([fronts[j] for j in range(len(fronts)) if fronts[j] == backs[j]]))
        fronts.extend(backs)
        fronts = list(set(fronts))
        try:
            return min([val for val in fronts if val not in prohibited])
        except:
            return 0
