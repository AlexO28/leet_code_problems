# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max_product = nums[0]
        if len(nums) > 1:
            local_max_product = nums[0]
            local_min_product = nums[0]
            for num in nums[1:]:
                num_1 = local_max_product * num
                num_2 = local_min_product * num
                local_max_product, local_min_product = max(num_1, num_2, num), min(num_2, num_1, num)
                global_max_product = max(global_max_product, local_max_product)
        return global_max_product
