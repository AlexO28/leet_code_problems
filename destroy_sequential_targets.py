# You are given a 0-indexed array nums consisting of positive integers, representing targets on a number line. You are also given an integer space.
# You have a machine which can destroy targets. Seeding the machine with some nums[i] allows it to destroy all targets with values that can be represented as nums[i] + c * space, where c is any non-negative integer. You want to destroy the maximum number of targets in nums.
# Return the minimum value of nums[i] you can seed the machine with to destroy the maximum number of targets.
class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        nums.sort()
        freq_dict = {}
        max_val = -1
        for num in nums:
            val = num % space
            if val in freq_dict:
                freq_dict[val] += 1
            else:
                freq_dict[val] = 1
            max_val = max(max_val, freq_dict[val])
        remainders = set()
        for elem in freq_dict:
            if freq_dict[elem] == max_val:
                remainders.add(elem)
        for elem in nums:
            if elem % space in remainders:
                return elem
