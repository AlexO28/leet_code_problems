# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
# If the current number is even, you have to divide it by 2.
# If the current number is odd, you have to add 1 to it.
# It is guaranteed that you can always reach one for all test cases.
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        number_of_steps = 0
        while True:
            if num == 1:
                return number_of_steps
            else:
                number_of_steps += 1
                num1, num2 = divmod(num, 2)
                if num2 == 0:
                    num = num1
                else:
                    num += 1 
