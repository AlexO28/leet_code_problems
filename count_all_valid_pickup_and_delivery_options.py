# Given n orders, each order consists of a pickup and a delivery service.
# Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 
# Since the answer may be too large, return it modulo 10^9 + 7.
class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            MOD = 10**9 + 7
            res = 1
            for i in range(2, n + 1):
                res = (res * i * (2 * i - 1)) % MOD
            return res
