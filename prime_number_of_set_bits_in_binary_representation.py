# Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.
# Recall that the number of set bits an integer has is the number of 1's present when written in binary.
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for j in range(left, right+1):
            num = self.number_of_units(j)
            if num in [2, 3, 5, 7, 11, 13, 17, 19]:
                count += 1
        return count

    def number_of_units(self, num):
        return len([elem for elem in list(bin(num)) if elem == "1"])
