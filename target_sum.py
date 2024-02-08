# You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return len([num for num in self.evaluateExpressions(nums) if num == target])

    def evaluateExpressions(self, nums):
        if len(nums) == 1:
            return [nums[0], - nums[0]]
        else:
            res = self.evaluateExpressions(nums[1:])
            res_fin = []
            for r in res:
                res_fin.append(nums[0] + r)
                res_fin.append(-nums[0] + r)
        return res_fin
