# You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.
# Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.
# Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.
# The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.
from math import inf


class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_pos = expression.find("+")
        min_val = inf
        phrase = ""
        for i in range(plus_pos):
            for j in range(plus_pos + 1, len(expression)):
                if i == 0:
                    num1 = 1
                else:
                    num1 = int(expression[:i])
                if j == len(expression) - 1:
                    num3 = 1
                else:
                    num3 = int(expression[(j + 1):])
                num2 = eval(expression[i:(j + 1)])
                candidate = num1 * num2 * num3
                if min_val > candidate:
                    min_val = candidate
                    phrase = "(" + expression[i:(j + 1)] + ")"
                    if i > 0:
                        phrase = expression[:i] + phrase
                    if j < len(expression) - 1:
                        phrase = phrase + expression[(j + 1):]
        return phrase
