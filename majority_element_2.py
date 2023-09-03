# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_dict = {}
        for num in nums:
            if num not in num_dict.keys():
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        res = []
        for num in num_dict.keys():
            if num_dict[num] > int(len(nums)/3):
                res.append(num)
        return res
