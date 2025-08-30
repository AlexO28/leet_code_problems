# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        summa = 0
        for num in nums:
            number_of_divisors = 0
            cur_sum = 0
            for i in range(1, int(num**0.5) + 1):
                main_part, remainder = divmod(num, i)
                if remainder == 0:
                    if main_part == i:
                        number_of_divisors += 1
                        cur_sum += 2 * i
                    else:
                        number_of_divisors += 2
                        cur_sum += i + main_part
                    if number_of_divisors > 4:
                        break
            if number_of_divisors == 4:
                summa += cur_sum
        return summa
