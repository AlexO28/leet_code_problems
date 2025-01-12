# A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
# It is ().
# It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
# It can be written as (A), where A is a valid parentheses string.
# You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
# If locked[i] is '1', you cannot change s[i].
# But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# Return true if you can make s a valid parentheses string. Otherwise, return false.
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        number_of_locked_open = 0
        number_of_unlocked = 0
        for i in range(len(s)):
            if locked[i] == "0":
                number_of_unlocked += 1
            else:
                if s[i] == "(":
                    number_of_locked_open += 1
                else:
                    if number_of_locked_open > 0:
                        number_of_locked_open -= 1
                    elif number_of_unlocked > 0:
                        number_of_unlocked -= 1
                    else:
                        return False
        if number_of_unlocked < number_of_locked_open:
            return False
        else:
            if (number_of_unlocked - number_of_locked_open) % 2 == 1:
                return False
        number_of_locked_open = 0
        number_of_unlocked = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == "0":
                number_of_unlocked += 1
            else:
                if s[i] == ")":
                    number_of_locked_open += 1
                else:
                    if number_of_locked_open > 0:
                        number_of_locked_open -= 1
                    elif number_of_unlocked > 0:
                        number_of_unlocked -= 1
                    else:
                        return False
        if number_of_unlocked < number_of_locked_open:
            return False
        else:
            if (number_of_unlocked - number_of_locked_open) % 2 == 1:
                return False
        return True
