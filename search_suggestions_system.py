# You are given an array of strings products and a string searchWord.
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
# Return a list of lists of the suggested products after each character of searchWord is typed.
from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        res = []
        for j in range(len(searchWord)):
            new_products = []
            for product in products:
                if len(product) > j:
                    if product[j] == searchWord[j]:
                        new_products.append(product)
            new_products.sort()
            res.append(new_products[:3])
            products = new_products.copy()
        return res
