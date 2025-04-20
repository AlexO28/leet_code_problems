# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.
# It is guaranteed that the given expression is valid and follows the given rules.
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []      
        for char in expression:
            if char in "tf!&|":
                stack.append(char)
            elif char == ")":
                true_count = 0
                false_count = 0
                while stack[-1] in "tf":
                    true_count += (stack[-1] == "t")
                    false_count += (stack[-1] == "f")
                    stack.pop()
                if len(stack) == 0:
                    if true_count > 0:
                        stack.append("t")
                    else:
                        stack.append("f")
                else:
                    operator = stack.pop()
                    print(operator)
                    if operator == "!":
                        if false_count > 0:
                            result_char = "t"
                        else:
                            result_char = "f"
                    elif operator == '&':
                        if false_count > 0:
                            result_char = "f"
                        else:
                            result_char = "t"
                    elif operator == "|":
                        if true_count > 0:
                            result_char = "t"
                        else:
                            result_char = "f"              
                    stack.append(result_char)
        return stack[0] == "t"
