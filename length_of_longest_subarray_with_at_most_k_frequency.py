# You are given an integer array nums and an integer k.
# The frequency of an element x is the number of times it occurs in an array.
# An array is called good if the frequency of each element in this array is less than or equal to k.
# Return the length of the longest good subarray of nums.
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_dict = {}
        max_num = 0
        left_ind = 0
        for right_ind in range(len(nums)):
            if nums[right_ind] in freq_dict:
                freq_dict[nums[right_ind]] += 1
            else:
                freq_dict[nums[right_ind]] = 1
            while freq_dict[nums[right_ind]] > k:
                freq_dict[nums[left_ind]] -= 1
                if freq_dict[nums[left_ind]] == 0:
                    del freq_dict[nums[left_ind]]
                left_ind += 1
            max_num = max(right_ind - left_ind + 1, max_num)
        return max_num
