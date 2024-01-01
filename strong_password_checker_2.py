# A password is said to be strong if it satisfies all the following criteria:
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        has_lower = 1
        has_upper = 1
        has_digit = 1
        has_else = 1
        prev_symb = "_"
        for symb in password:
            if symb.islower():
                has_lower = 0
            elif symb.isupper():
                has_upper = 0
            elif symb.isdigit():
                has_digit = 0
            else:
                has_else = 0
            if symb == prev_symb:
                return False
            else:
                prev_symb = symb
        return has_lower + has_upper + has_digit + has_else == 0
  
