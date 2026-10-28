# You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].
# The array describes transactions, where each transaction must be completed exactly once in some order. At any given moment, you have a certain amount of money. In order to complete transaction i, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.
# Return the minimum amount of money required before any transaction so that all of the transactions can be completed regardless of the order of the transactions.
class Solution:
    def minimumMoney(self, transactions: list[list[int]]) -> int:
        s = sum(max(0, a - b) for a, b in transactions)
        res = 0
        for a, b in transactions:
            if a > b:
                res = max(res, s + b)
            else:
                res = max(res, s + a)
        return res
