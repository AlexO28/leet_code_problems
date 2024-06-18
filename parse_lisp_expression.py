# You are given a string expression representing a Lisp-like expression to return the integer value of.
# The syntax for these expressions is given as follows.
# An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer.
# (An integer could be positive or negative.)
# A let expression takes the form "(let v1 e1 v2 e2 ... vn en expr)", where let is always the string "let", then there are one or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let expression is the value of the expression expr.
# An add expression takes the form "(add e1 e2)" where add is always the string "add", there are always two expressions e1, e2 and the result is the addition of the evaluation of e1 and the evaluation of e2.
# A mult expression takes the form "(mult e1 e2)" where mult is always the string "mult", there are always two expressions e1, e2 and the result is the multiplication of the evaluation of e1 and the evaluation of e2.
# For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names "add", "let", and "mult" are protected and will never be used as variable names.
# Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.
from collections import defaultdict


class Solution:
    def evaluate(self, expression: str) -> int:
        self.index = 0
        self.scope = defaultdict(list)
        self.expression = expression
        return self.evaluate_expression()

    def parse_variable(self):
        start = self.index
        while (self.index < len(self.expression)) and (self.expression[self.index] not in " )"):
            self.index += 1
        return self.expression[start:self.index]

    def parse_integer(self):
        sign = 1
        value = 0
        if self.expression[self.index] == "-":
            sign = -1
            self.index += 1
        while (self.index < len(self.expression)) and self.expression[self.index].isdigit():
            value = value * 10 + int(self.expression[self.index])
            self.index += 1
        return sign * value

    def evaluate_expression(self):
        if self.expression[self.index] != "(":
            if self.expression[self.index].islower():
                parsed_variable = self.parse_variable()
                return self.scope[parsed_variable][-1]
            else:
                return self.parse_integer()
        self.index += 1
        if self.expression[self.index] == "l":
            self.index += 4
            variables = []
            while True:
                var = self.parse_variable()
                if self.expression[self.index] == ")":
                    result = self.scope[var][-1]
                    break
                variables.append(var)
                self.index += 1
                self.scope[var].append(self.evaluate_expression())
                self.index += 1
                if not self.expression[self.index].islower():
                    result = self.evaluate_expression()
                    break
            for var in variables:
                self.scope[var].pop()
        else:
            is_add = (self.expression[self.index] == "a") 
            if is_add:
                self.index += 4
            else:
                self.index += 5
            first_operand = self.evaluate_expression()
            self.index += 1
            second_operand = self.evaluate_expression()
            if is_add:
                result = first_operand + second_operand 
            else:
                result = first_operand * second_operand
        self.index += 1
        return result
