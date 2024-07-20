# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
# Given the array answers, return the minimum number of rabbits that could be in the forest.
import numpy  as np


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq_dict = {}
        for answer in answers:
            if answer in freq_dict:
                freq_dict[answer] += 1
            else:
                freq_dict[answer] = 1
        number_of_rabbits = 0
        for answer in freq_dict.keys():
            number_of_rabbits += np.ceil(freq_dict[answer]/(answer+1))*(answer+1)
        return int(number_of_rabbits)
