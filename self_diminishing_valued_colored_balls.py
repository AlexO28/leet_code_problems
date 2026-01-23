# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.
# The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).
# You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.
# Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        mod = 1000000007
        ans = 0
        i = 0
        while orders > 0:
            while i < len(inventory) and inventory[i] >= inventory[0]:
                i += 1
            nxt = 0
            if i < len(inventory):
                nxt = inventory[i]
            cnt = i
            x = inventory[0] - nxt
            tot = cnt * x
            if tot > orders:
                decr = orders // cnt
                a1 = inventory[0] - decr + 1
                an = inventory[0]
                ans += (a1 + an) * decr // 2 * cnt
                ans += (inventory[0] - decr) * (orders % cnt)
            else:
                a1 = nxt + 1
                an = inventory[0]
                ans += (a1 + an) * x // 2 * cnt
                inventory[0] = nxt
            orders -= tot
            ans %= mod
        return ans
