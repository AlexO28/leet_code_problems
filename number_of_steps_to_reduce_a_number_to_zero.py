# Given an integer num, return the number of steps to reduce it to zero.
#  In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
class Solution:
    def numberOfSteps(self, num: int) -> int:
        number_of_steps = 0
        while num > 0:
            number_of_steps += 1
            main_part, remainder = divmod(num, 2)
            if remainder == 0:
                num = main_part
            else:
                num -= 1
        return number_of_steps
