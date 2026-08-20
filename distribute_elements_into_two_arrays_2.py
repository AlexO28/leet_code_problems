# You are given a 1-indexed array of integers nums of length n.
# We define a function greaterCount such that greaterCount(arr, val) returns the number of elements in arr that are strictly greater than val.
# You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:
# If greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]), append nums[i] to arr1.
# If greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]), append nums[i] to arr2.
# If greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]), append nums[i] to the array with a lesser number of elements.
# If there is still a tie, append nums[i] to arr1.
# The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].
# Return the integer array result.
from typing import List
from sortedcontainers import SortedList


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = SortedList([nums[0]])
        arr2 = SortedList([nums[1]])
        arr1_unsorted = [nums[0]]
        arr2_unsorted = [nums[1]]
        for i in range(2, len(nums)):
            quantity1 = len(arr1) - arr1.bisect_right(nums[i])
            quantity2 = len(arr2) - arr2.bisect_right(nums[i])
            if quantity1 > quantity2:
                arr1.add(nums[i])
                arr1_unsorted.append(nums[i])
            elif quantity1 < quantity2:
                arr2.add(nums[i])
                arr2_unsorted.append(nums[i])
            elif len(arr1_unsorted) <= len(arr2_unsorted):
                arr1.add(nums[i])
                arr1_unsorted.append(nums[i])
            else:
                arr2.add(nums[i])
                arr2_unsorted.append(nums[i])
        arr1_unsorted.extend(arr2_unsorted)
        return arr1_unsorted
