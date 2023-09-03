# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        num_dict = {}
        for j in range(len(nums)):
            if nums[j] not in num_dict.keys():
                num_dict[nums[j]] = [j]
            else:
                max_val = max(num_dict[nums[j]])
                if j - max_val <= k:
                    return True
                else:
                    num_dict[nums[j]].append(j)
        return False
