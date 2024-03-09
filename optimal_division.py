# You are given an integer array nums. The adjacent integers in nums will perform the float division.
# For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
# However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.
# Return the corresponding expression that has the maximum value in string format.
# Note: your expression should not contain redundant parenthesis.
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        return self.bestDivision(nums, True)[1]

    def bestDivision(self, nums, searchMax):
        if len(nums) == 2:
            return nums[0]/nums[1], str(nums[0]) + "/" + str(nums[1])
        first_val, first_expr = self.bestDivision(nums[1:], not searchMax)
        second_val, second_expr = self.bestDivision(nums[:(-1)], searchMax)
        first_val = nums[0]/first_val
        second_val = second_val/nums[-1]
        if first_val > second_val:
            if searchMax:
                return first_val, str(nums[0]) + "/" + "(" + first_expr + ")"
            else:
                return second_val, second_expr + "/" + str(nums[-1])
        else:
            if searchMax:
                return second_val, second_expr + "/" + str(nums[-1])
            else:
                return first_val, str(nums[0]) + "/" + "(" + first_expr + ")"
