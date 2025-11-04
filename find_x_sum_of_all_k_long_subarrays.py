# You are given an array nums of n integers and two integers k and x.
# The x-sum of an array is calculated by the following procedure:
# Count the occurrences of all elements in the array.
# Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
# Calculate the sum of the resulting array.
# Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
# Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
import numpy as np
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            freq_dict = {}
            for j in range(i, i + k):
                if nums[j] in freq_dict:
                    freq_dict[nums[j]] += 1
                else:
                    freq_dict[nums[j]] = 1
            inv_dict = {}
            for key in freq_dict:
                if freq_dict[key] in inv_dict:
                    inv_dict[freq_dict[key]].append(key)
                else:
                    inv_dict[freq_dict[key]] = [key]
            values = list(inv_dict.keys())
            values.sort(reverse=True)
            count = 0
            summa = 0
            found = False
            for val in values:
                arr = inv_dict[val]
                arr.sort(reverse=True)
                for elem in arr:
                    summa += elem * val
                    count += 1
                    if count == x:
                        found = True
                        break
                if found:
                    break
            res.append(summa)
        return res
