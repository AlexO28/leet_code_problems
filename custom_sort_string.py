# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
# Return any permutation of s that satisfies this property.
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        if len(s) == 1:
            return s
        order_dict = {}
        for j in range(len(order)):
            order_dict[order[j]] = j
        max_val = len(order)
        def sort_fun(x):
            if x in order_dict:
                return order_dict[x]
            else:
                return len(order)
        s = list(s)
        s.sort(key=sort_fun)
        return ''.join(s)
