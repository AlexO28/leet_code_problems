# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

  
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = []       
        while True:
            if n == 1:
                return True
            visited.append(n)
            digits = list(str(n))
            n_new = sum([int(d) ** 2 for d in digits])
            if n_new in visited:
                return False
            else:
                n = n_new
