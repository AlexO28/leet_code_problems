# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        number_of_zeros = len([num for num in nums if num == 0])
        if number_of_zeros > 1:
            return [0]*len(nums)
        elif number_of_zeros == 1:
            arr = [0]*len(nums)
            index = nums.index(0)
            prod = 1
            for j in range(len(nums)):
                if (j != index):
                    prod *= nums[j]
            arr[index] = int(prod)
        else:
            prod = 1
            for j in range(len(nums)):
                prod *= nums[j]
            arr = [0]*len(nums)
            for j in range(len(nums)):
               arr[j] = int(prod/nums[j])
        return arr
