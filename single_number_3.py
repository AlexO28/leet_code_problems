# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        nums.sort()
        elements = []
        search_couple = False
        for j in range(len(nums)):
            if search_couple:
                if nums[j] == prev_elem:
                    search_couple = False
                else:
                    elements.append(prev_elem)
                    if len(elements) == 2:
                        return elements
                    prev_elem = nums[j]
            else:
                prev_elem = nums[j]
                search_couple = True
        elements.append(nums[-1])
        return elements
