# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).


class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([elem for elem in list("{0:b}".format(n)) if elem == '1'])
