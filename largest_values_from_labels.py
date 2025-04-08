# You are given n item's value and label as two integer arrays values and labels. You are also given two integers numWanted and useLimit.
# Your task is to find a subset of items with the maximum sum of their values such that:
# The number of items is at most numWanted.
# The number of items with the same label is at most useLimit.
# Return the maximum sum.
import numpy as np
from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        labels = np.array(labels)
        values = np.array(values)
        arg_inds = values.argsort()[::-1]
        labels = labels[arg_inds]
        values = values[arg_inds]
        limit_dict = {}
        max_sum = 0
        if useLimit == 0:
            return int(max_sum)
        number_of_elements = 0
        for j in range(len(values)):
            if number_of_elements == numWanted:
                return int(max_sum)
            if labels[j] in limit_dict:
                if limit_dict[labels[j]] < useLimit:
                    limit_dict[labels[j]] += 1
                    max_sum += values[j]
                    number_of_elements += 1
            else:
                limit_dict[labels[j]] = 1
                max_sum += values[j]
                number_of_elements += 1
        return int(max_sum)
