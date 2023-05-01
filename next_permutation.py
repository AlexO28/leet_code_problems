# generate next valid permutation in the lexigoraphical order, if impossible return the initial one

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        found = False
        for i in range(len(nums)-1):
            index = len(nums)-i-2
            if nums[index] < nums[index + 1]:
                found = True
                break
        if not found:
            nums.sort()
        else:
            for j in range(len(nums) - index - 1):
                if nums[len(nums) - j - 1] > nums[index]:
                    new_index = len(nums) - j - 1
                    break
            nums[index], nums[new_index] = nums[new_index], nums[index]
            if index+1 <=  len(nums)-2:
                if nums[index+2] > nums[index+1]:
                    nums[(index+1):] = sorted(nums[(index+1):], reverse = True)
                else:
                    nums[(index+1):] = sorted(nums[(index+1):])
       
