# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.
# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right+1):
            num_str = str(num)
            fine = True
            if "0" not in num_str:
                for digit in range(2, 10):
                    if str(digit) in num_str:
                        if num % digit > 0:
                            fine = False
                    if not fine:
                        break
                if fine:
                    res.append(num)
        return res
