# You are given two integer arrays nums1 and nums2.
# We say that nums2 is reachable from nums1 with an integer x if there exist two elements in nums1 that, when removed, and x is added to all the remaining elements of nums1 (or subtracted in the case of a negative x), the resulting array becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.
# Return the minimum possible integer x that makes nums2 reachable from nums1.
# It is guaranteed that nums2 is reachable from nums1 with at least one x.
from typing import List
from math import inf
from collections import Counter


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        freq_dict_1 = Counter(nums1)
        freq_dict_2 = Counter(nums2)
        target_sum = sum(nums2)
        big_sum = sum(nums1)
        found_x = inf
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                main_part, remainder = divmod((big_sum - nums1[i] - nums1[j] - target_sum), len(nums1) - 2)
                if remainder == 0:
                    freq_dict_1[nums1[i]] -= 1
                    freq_dict_1[nums1[j]] -= 1
                    for key in freq_dict_2:
                        alt_key = key + main_part
                        if alt_key not in freq_dict_1:
                            break
                        else:
                            if freq_dict_1[alt_key] != freq_dict_2[key]:
                                break
                    else:
                        found_x = min(found_x, -main_part) 
                    freq_dict_1[nums1[i]] += 1
                    freq_dict_1[nums1[j]] += 1
        return found_x
