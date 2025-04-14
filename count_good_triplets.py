# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        number_of_good_triplets = 0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            number_of_good_triplets += 1
        return number_of_good_triplets 
