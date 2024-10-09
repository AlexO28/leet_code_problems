# A parentheses string is valid if and only if:
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        number_of_open = 0
        number_of_close = 0
        discrepancy = 0
        cur_discrepancy = 0
        for elem in s:
            if elem == "(":
                discrepancy += cur_discrepancy
                cur_discrepancy = 0
                number_of_open = max(0, number_of_open-number_of_close)
                number_of_open += 1
                number_of_close = 0
            else:
                number_of_close += 1
                cur_discrepancy = max(cur_discrepancy, number_of_close-number_of_open)
        return discrepancy + abs(number_of_open-number_of_close)
