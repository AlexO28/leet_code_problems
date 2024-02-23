# Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
# A good subarray is a subarray where:
# its length is at least two, and
# the sum of the elements of the subarray is a multiple of k.
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        prefix_sum = 0
        mod_index_map = {0: -1}
        for j in range(len(nums)):
            prefix_sum += nums[j]
            modulus = prefix_sum % k
            if modulus in mod_index_map:
                if j - mod_index_map[modulus] >= 2:
                    return True
            else:
                mod_index_map[modulus] = j
        return False
