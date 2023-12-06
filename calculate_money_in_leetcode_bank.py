# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
class Solution:
    def totalMoney(self, n: int) -> int:
        a, b = divmod(n, 7)
        first_part = a * 28
        second_part = (a-1)*a*7/2
        if b > 0:
            b -= 1
            third_part = (b + 1) * a + (b+2)*(b+1)/2
        else:
            third_part = 0
        return int(first_part + second_part + third_part)
 
