# You are given two positive integers num and sum.
# A positive integer n is good if it satisfies both of the following:
# The number of digits in n is exactly num.
# The sum of digits in n is exactly sum.
# The score of a good integer n is the sum of the squares of digits in n.
# Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = []
        for j in range(num):
            if sum <= 0:
                res.append("0")
            else:
                for candidate in range(9, 0, -1):
                    if sum >= candidate:
                        sum -= candidate
                        res.append(str(candidate))
                        break
        if sum > 0:
            return ""
        else:
            return "".join(res)
