# You are given a valid boolean expression as a string expression consisting of the characters '1','0','&' (bitwise AND operator),'|' (bitwise OR operator),'(', and ')'.
# For example, "()1|1" and "(1)&()" are not valid while "1", "(((1))|(0))", and "1|(0&(1))" are valid expressions.
# Return the minimum cost to change the final value of the expression.
# For example, if expression = "1|1|(0&0)&1", its value is 1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1. We want to apply operations so that the new expression evaluates to 0.
# The cost of changing the final value of an expression is the number of operations performed on the expression. The types of operations are described as follows:
# Turn a '1' into a '0'.
# Turn a '0' into a '1'.
# Turn a '&' into a '|'.
# Turn a '|' into a '&'.
# Note: '&' does not take precedence over '|' in the order of calculation. Evaluate parentheses first, then in left-to-right order.
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        operand_stack = []
        operator_stack = []
        for ch in expression:
            if ch == " ":
                continue
            if ch == "(":
                operator_stack.append(ch)
            elif ch == "0" or ch == "1":
                if ch == "0":
                    operand_stack.append((0, 1))
                else:
                    operand_stack.append((1, 0))
            elif ch in "&|":
                while operator_stack and operator_stack[-1] in "&|":
                    op = operator_stack.pop()
                    right = operand_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(self.combine(left, op, right))
                operator_stack.append(ch)
            elif ch == ")":
                while operator_stack and operator_stack[-1] != "(":
                    op = operator_stack.pop()
                    right = operand_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(self.combine(left, op, right))
                operator_stack.pop()
        while operator_stack:
            op = operator_stack.pop()
            right = operand_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(self.combine(left, op, right))
        final_dp = operand_stack[-1]
        if final_dp[0] < final_dp[1]:
            final_value = 0
        else:
            final_value = 1
        if final_value == 0:
            return final_dp[1]
        else:
            return final_dp[0]

    def combine(self, left, op, right):
        if op == "&":
            cost_keep_1 = left[1] + right[1]
            cost_keep_0 = min(
                left[0] + right[0], left[0] + right[1], left[1] + right[0]
            )
            cost_flip_0 = left[0] + right[0]
            cost_flip_1 = min(
                left[1] + right[0], left[0] + right[1], left[1] + right[1]
            )
        else:
            cost_keep_0 = left[0] + right[0]
            cost_keep_1 = min(
                left[1] + right[0], left[0] + right[1], left[1] + right[1]
            )
            cost_flip_1 = left[1] + right[1]
            cost_flip_0 = min(
                left[0] + right[0], left[0] + right[1], left[1] + right[0]
            )
        final0 = min(cost_keep_0, 1 + cost_flip_0)
        final1 = min(cost_keep_1, 1 + cost_flip_1)
        return (final0, final1)
