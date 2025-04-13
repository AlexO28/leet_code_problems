# Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.
# The grammar can best be understood through simple examples:
# Single letters represent a singleton set containing that word.
# R("a") = {"a"}
# R("w") = {"w"}
# When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
# R("{a,b,c}") = {"a","b","c"}
# R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
# When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
# R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
# R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
# Formally, the three rules for our grammar:
# For every lowercase letter x, we have R(x) = {x}.
# For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
# For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
# Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.
from typing import List


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        self.expanded_set = set()
        self.search(expression)
        return sorted(self.expanded_set)


    def search(self, expr):
        closing_index = expr.find("}")
        if closing_index == -1:
            self.expanded_set.add(expr)
        else:
            opening_index = expr.rfind("{", 0, closing_index)
            before_brace = expr[:opening_index]
            after_brace = expr[(closing_index + 1):]
            lines = expr[(opening_index + 1):closing_index].split(",")
            for inside_brace in lines:
                self.search(before_brace + inside_brace + after_brace)
