# Given an integer array nums and two integers k and p, return the number of distinct subarrays, which have at most k elements that are divisible by p.
# Two arrays nums1 and nums2 are said to be distinct if:
# They are of different lengths, or
# There exists at least one index i where nums1[i] != nums2[i].
# A subarray is defined as a non-empty contiguous sequence of elements in an array.
class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        nums_set = set()
        for i in range(len(nums)):
            cur_arr = []
            for j in range(i, len(nums)):
                cur_arr.append(nums[j])
                nums_set.add(tuple(cur_arr))
        res = 0
        for cur_tuple in nums_set:
            num_of_elements = 0
            for elem in cur_tuple:
                if elem % p == 0:
                    num_of_elements += 1
                    if num_of_elements > k:
                        break
            else:
                res += 1
        return res
