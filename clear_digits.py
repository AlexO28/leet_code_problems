# You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
class Solution:
    def clearDigits(self, s: str) -> str:
        non_digits = []
        for elem in s:
            if elem.isdigit():
                if len(non_digits) > 0:
                    non_digits.pop()
            else:
                non_digits.append(elem)
        return "".join(non_digits)
