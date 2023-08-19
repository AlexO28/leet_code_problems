# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for j in range(len(numbers)):
            if numbers[j] not in dict.keys():
                dict[numbers[j]] = [j]
            else:
                dict[numbers[j]].append(j)
        for j in range(len(numbers)):
            if (target - numbers[j]) in dict.keys():
                arr = dict[target - numbers[j]]
                if len(arr) <= 2:
                   arr = [x for x in arr if x != j]
                   if len(arr) > 0:
                       return [1+j, 1+arr[0]]
