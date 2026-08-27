# You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.
# Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.
# Return the minimum number of magic beans that you have to remove.
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        if len(beans) == 1:
            return 0
        beans.sort()
        summa = sum(beans)
        n = len(beans)
        return min(summa - x * (n - i) for i, x in enumerate(beans))
