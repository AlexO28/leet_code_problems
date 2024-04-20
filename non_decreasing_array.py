# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        number_of_violations = 0
        violation_index = -1
        for j in range(1, len(nums)):
            if nums[j] < nums[j-1]:
                violation_index = j
                number_of_violations += 1
                if number_of_violations > 1:
                    return False
        if number_of_violations == 0:
            return True
        save = nums[violation_index]
        nums[violation_index] = nums[j-1]
        check = True
        for j in range(violation_index, len(nums)):
            if nums[j] < nums[j-1]:
                check = False
        if check:
            return True
        nums[violation_index] = save
        save = nums[violation_index-1]
        nums[violation_index-1] = nums[violation_index]
        check = True
        for j in range(max(1, violation_index-1), len(nums)):
            if nums[j] < nums[j-1]:
                check = False
                break
        if check:
            return True
        if violation_index == len(nums)-1:
            return False
        nums[violation_index-1] = save
        nums[violation_index] = nums[violation_index+1] 
        for j in range(violation_index, len(nums)):
            if nums[j] < nums[j-1]:
                return False
        return True
