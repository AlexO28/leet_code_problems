# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


import math


def find_permutations(nums):
    if len(nums) == 1:
        return [nums]
    results = []
    detected_elements = []
    max_len = math.factorial(len(nums))
    for j in range(len(nums)):
        if nums[j] not in detected_elements:
            detected_elements.append(nums[j])
        else:
            continue
        if j == 0:
            temp_res = find_permutations(nums[1:])
        elif j == len(nums) - 1:
            temp_res = find_permutations(nums[:(len(nums)-1)])
        else:
            temp_res = find_permutations(nums[:j] + nums[(j+1):])
        for temp_elem in temp_res:
            if [nums[j]] + temp_elem not in results:
                results.append([nums[j]] + temp_elem)
            if temp_elem + [nums[j]] not in results:
                results.append(temp_elem + [nums[j]])
            if len(temp_elem) > 1:
                for k in range(1, len(temp_elem)):
                    if temp_elem[:k] + [nums[j]] + temp_elem[k:] not in results:
                        results.append(temp_elem[:k] + [nums[j]] + temp_elem[k:])
            if len(results) == max_len:
                return results
    return results


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return find_permutations(nums)
