# You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq_dict = {}
        max_freq = 0
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
            max_freq = max(max_freq, freq_dict[num])
        buckets = []
        for j in range(max_freq):
            bucket = []
            for key in freq_dict.keys():
                if freq_dict[key] >= j + 1:
                    bucket.append(key)
            buckets.append(bucket)
        return buckets
