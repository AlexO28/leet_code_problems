# You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.
# Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
# Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
# Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
# Return the maximum possible score you can achieve after playing any number of tokens.
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left_index = 0
        right_index =len(tokens) - 1
        max_score = 0
        current_score = 0
        while left_index <= right_index:
            if power >= tokens[left_index]:
                power -= tokens[left_index]
                left_index += 1
                current_score += 1
                max_score = max(max_score, current_score)
            elif current_score > 0:
                power += tokens[right_index]
                right_index -= 1
                current_score -= 1
            else:
                break              
        return max_score
