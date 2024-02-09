class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        numbers = [0, 1]
        for i in range(2, n+1):
            numbers.append(numbers[-1] + numbers[-2])
        return numbers[-1]
 
