# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            try:
                num = int(token)
                numbers.append(num)
            except:
                last_token = numbers.pop(len(numbers)-1)
                pre_last_token = numbers.pop(len(numbers)-1)
                if token == "+":
                    numbers.append(last_token + pre_last_token)
                elif token == "-":
                    numbers.append(pre_last_token - last_token)
                elif token == "*":
                    numbers.append(pre_last_token * last_token)
                elif token == "/":
                    numbers.append(int(pre_last_token/last_token))
        return numbers[-1]
