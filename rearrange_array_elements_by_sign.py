# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should rearrange the elements of nums such that the modified array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        res = []
        for j in range(len(positives)):
            res.append(positives[j])
            res.append(negatives[j])
        return res
