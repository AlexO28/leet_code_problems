# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.


class Solution:
    def compute(self, expr):
        if ("+" not in expr) and ("-" not in expr) and ("*" not in expr):
            return [int(expr)]
        else:
            res = []
            for i in range(len(expr)):
                if expr[i] in ["+", "-", "*"]:
                    res_left = self.compute(expr[:i])
                    res_right = self.compute(expr[(i+1):])
                    for elem_left in res_left:
                        for elem_right in res_right:
                            res.append(eval(str(elem_left) + expr[i] + str(elem_right)))
            return res

    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.compute(expression)
