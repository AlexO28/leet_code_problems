# There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:
# Eat one orange.
# If the number of remaining oranges n is divisible by 2 then you can eat n / 2 oranges.
# If the number of remaining oranges n is divisible by 3 then you can eat 2 * (n / 3) oranges.
# You can only choose one of the actions per day.
# Given the integer n, return the minimum number of days to eat n oranges.
from functools import cache


class Solution:
    def minDays(self, n: int) -> int:
        return self.calculate(n)

    @cache
    def calculate(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            main_part_2, remainder_2 = divmod(n, 2)
            main_part_3, remainder_3 = divmod(n, 3)
            return 1 + min(
                remainder_2 + self.calculate(main_part_2),
                remainder_3 + self.calculate(main_part_3),
            )
