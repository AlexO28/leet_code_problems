# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores_sorted = score.copy()
        scores_sorted.sort(reverse=True)
        scores_dict = {}
        scores_dict[scores_sorted[0]] = "Gold Medal"
        if len(score) > 1:
            scores_dict[scores_sorted[1]] = "Silver Medal"
        if len(score) > 2:
            scores_dict[scores_sorted[2]] = "Bronze Medal"
        if len(score) > 3:
            for j in range(3, len(scores_sorted)):
                scores_dict[scores_sorted[j]] = str(j+1)
        return [scores_dict[val] for val in score]
