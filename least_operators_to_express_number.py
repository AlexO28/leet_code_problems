# Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.
# When writing such an expression, we adhere to the following conventions:
# The division operator (/) returns rational numbers.
# There are no parentheses placed anywhere.
# We use the usual order of operations: multiplication and division happen before addition and subtraction.
# It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
# We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.
from functools import cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        return self.search(x, target)        

    @cache
    def search(self, x, current_value):
        if x >= current_value:
            return min(current_value * 2 - 1, (x - current_value) * 2)
        else:
            k = 2
            pow_init = x ** 2 
            while pow_init < current_value:
                pow_init *= x
                k += 1
            if pow_init - current_value < current_value:
                return min(k + self.search(x, pow_init - current_value), 
                           k - 1 + self.search(x, current_value - int(pow_init/x)))
            else:
                return k - 1 + self.search(x, current_value - int(pow_init/x))
