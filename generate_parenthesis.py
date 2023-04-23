# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = ['(']
        used_open = [1]
        used_closed = [0]
        for i in range(2*n-1):
            num = len(combinations)
            for j in range(num):
                if (used_open[j] < n) & (used_closed[j] < n):
                    if used_open[j] > used_closed[j]:
                        combinations.append(combinations[j] + ')')
                        used_open.append(used_open[j])
                        used_closed.append(used_closed[j] + 1)
                        combinations[j] += '('
                        used_open[j] += 1
                    else:
                        combinations[j] += '('
                        used_open[j] += 1
                else:
                    combinations[j] += ')'
                    used_closed[j] += 1
        return combinations
