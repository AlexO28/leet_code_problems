# Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.
# The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
# Any two characters may be swapped, even if they are not adjacent.
class Solution:
    def minSwaps(self, s: str) -> int:
        discrepancies_1 = 0
        discrepancies_2 = 0
        number_of_ones = 0
        number_of_zeros = 0
        for j in range(len(s)):
            if j % 2 == 0:
                if s[j] == "1":
                    discrepancies_1 += 1
                    number_of_ones += 1
                else:
                    discrepancies_2 += 1
                    number_of_zeros += 1
            else:
                if s[j] == "1":
                    discrepancies_2 += 1
                    number_of_ones += 1
                else:
                    discrepancies_1 += 1
                    number_of_zeros += 1
        if abs(number_of_ones - number_of_zeros) > 1:
            return -1
        main_part_1, remainder_1 = divmod(discrepancies_1, 2)
        main_part_2, remainder_2 = divmod(discrepancies_2, 2)
        if (remainder_1 == 1) and (remainder_2) == 1:
            return -1
        elif remainder_1 == 1:
            return main_part_2
        elif remainder_2 == 1:
            return main_part_1
        else:
            return min(main_part_1, main_part_2)
