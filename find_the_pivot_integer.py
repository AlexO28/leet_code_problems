# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
class Solution:
    def pivotInteger(self, n: int) -> int:
        res_squared = (((n ** 2 + n)/2))
        candidate = res_squared ** 0.5
        res = int(candidate)
        if res ** 2 == res_squared:
            return res
        else:
            return -1
