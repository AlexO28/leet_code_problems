# An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.
# Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(elem) for elem in list(str(n))]
        if len(digits) == 1:
            return n
        new_digits = digits.copy()
        some_problems = True
        while some_problems:
            some_problems = False
            for j in range(1, len(digits)):
                if new_digits[j] < new_digits[j-1]:
                    some_problems = True
                    found = False
                    for i in range(j-1, -1, -1):
                        if new_digits[i] > 0:
                            new_digits[i] -= 1
                            found = True
                            for k in range(j, len(new_digits)):
                                new_digits[k] = 9
                            break
                    if not found:
                        new_digits = [9]*(len(digits)-1) 
                    break
        return int("".join([str(elem) for elem in new_digits]))
