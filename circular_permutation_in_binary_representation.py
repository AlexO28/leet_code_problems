# Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
# p[0] = start
# p[i] and p[i+1] differ by only one bit in their binary representation.
# p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
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
        index = numbers.index(start)
        return numbers[index:] + numbers[:index]
