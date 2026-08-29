# You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).
# Return the largest possible value of num after any number of swaps.
class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(elem) for elem in str(num)]
        digits_even = []
        digits_odd = []
        for digit in digits:
            if digit % 2 == 1:
                digits_odd.append(digit)
            else:
                digits_even.append(digit)
        digits_even.sort(reverse = True)
        digits_odd.sort(reverse = True)
        res = []
        even_ind = 0
        odd_ind = 0
        for digit in digits:
            if digit % 2 == 1:
                res.append(digits_odd[odd_ind])
                odd_ind += 1
            else:
                res.append(digits_even[even_ind])
                even_ind += 1
        return int("".join([str(digit) for digit in res]))
