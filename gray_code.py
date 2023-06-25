# An n-bit gray code sequence is a sequence of 2n integers where:
# Every integer is in the inclusive range [0, 2n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.


class Solution:
    def grayCode(self, n: int) -> List[int]:
        string_numbers = []
        for j in range(1, n + 1):
            if j == 1:
                string_numbers.append(["0"]*n)
                string_numbers.append(["0"]*(n-1) + ["1"])
            else:
                cur_len = len(string_numbers)
                for k in range(cur_len):
                    next_list = []
                    for s in range(n):
                        if s < n-j:
                            next_list.append("0")
                        elif s == n-j:
                            next_list.append("1")
                        else:
                            next_list.append(string_numbers[cur_len-k-1][s])
                    string_numbers.append(next_list)
        numbers = []
        for string_number in string_numbers:
            line = ''.join(string_number)
            num = int(line, 2)
            numbers.append(num)
        return numbers
