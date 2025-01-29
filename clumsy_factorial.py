# The factorial of a positive integer n is the product of all positive integers less than or equal to n.
# We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.
# However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.
# Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.
# Given an integer n, return the clumsy factorial of n.
class Solution:
    def clumsy(self, n: int) -> int:
        res = []
        oper = 0
        for j in range(n, 0, -1):
            if j == n:
                res.append(str(j))
            else:
                if oper == 0:
                    res.append("*")
                elif oper == 1:
                    res.append("//")
                elif oper == 2:
                    res.append("+")
                elif oper == 3:
                    res.append("-")
                res.append(str(j))
                oper += 1
                if oper == 4:
                    oper = 0
        return eval("".join(res))
