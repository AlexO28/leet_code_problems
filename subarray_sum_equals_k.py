# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_dict = {}
        cur_sum = 0
        for j in range(len(nums)):
            cur_sum += nums[j]
            if cur_sum in freq_dict:
                freq_dict[cur_sum].append(j)
            else:
                freq_dict[cur_sum] = [j]
        number_of_combinations = 0
        for key in freq_dict.keys():
            if key == k:
                inds = freq_dict[key]
                number_of_combinations += len(inds)
            key_next = key + k
            if key_next in freq_dict.keys():
                if k != 0:
                    inds1 = freq_dict[key]
                    inds2 = freq_dict[key_next]
                    for i in inds1:
                        for j in inds2:
                            if j > i:
                                number_of_combinations += 1
                else:
                    inds = freq_dict[key]
                    if len(inds) > 0:
                        number_of_combinations += int(len(inds)*(len(inds)-1)/2)
        return number_of_combinations
