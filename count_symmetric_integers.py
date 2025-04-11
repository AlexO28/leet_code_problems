# You are given two positive integers low and high.
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.
# Return the number of symmetric integers in the range [low, high].
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        number_of_symmetric = 0
        for i in range(low, high+1):
            i_str = str(i)
            main_part, remainder = divmod(len(i_str), 2)
            if remainder == 0:
                if sum([int(i_str[j]) for j in range(main_part)]) == sum([int(i_str[j]) for j in range(main_part, len(i_str))]):
                    number_of_symmetric += 1
        return number_of_symmetric 
