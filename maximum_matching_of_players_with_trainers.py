# You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.
# The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.
# Return the maximum number of matchings between players and trainers that satisfy these conditions.
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ind_1 = 0
        ind_2 = 0
        number_of_matches = 0
        while (ind_1 < len(players)) and (ind_2 < len(trainers)):
            if players[ind_1] <= trainers[ind_2]:
                ind_1 += 1
                ind_2 += 1
                number_of_matches += 1
            else:
                ind_2 += 1
        return number_of_matches
