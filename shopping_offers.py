# In LeetCode Store, there are n items to sell. Each item has a price. However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price.
# You are given an integer array price where price[i] is the price of the ith item, and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.
# You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.
# Return the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers. You are not allowed to buy more items than you want, even if that would lower the overall price. You could use any of the special offers as many times as you want.
from functools import cache


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
       self.price = price
       self.special = special
       return self.applyShoppingOffers(','.join([str(need) for need in needs]))

    @cache
    def applyShoppingOffers(self, needs):
        needs = needs.split(',')
        needs = [int(need) for need in needs]
        min_price = sum([needs[j]*self.price[j] for j in range(len(needs))])
        for offer in self.special:
            new_needs = needs.copy()
            good = True
            for j in range(len(needs)):
                new_needs[j] -= offer[j]
                if new_needs[j] < 0:
                    good = False
                    break
            if good:
                cur_price = self.applyShoppingOffers(','.join([str(need) for need in new_needs])) + offer[-1]
                min_price = min(cur_price, min_price)
        return min_price
