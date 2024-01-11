# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        count = 0
        for i in range(max(len(x), len(y))):
            if (i < len(x)) & (i < len(y)):
                if x[len(x)-i-1] != y[len(y)-i-1]:
                    count += 1
            elif i < len(x):
                if x[len(x)-i-1] != "0":
                    count += 1
            else:
                if y[len(y)-i-1] != "0":
                    count += 1
        return count
