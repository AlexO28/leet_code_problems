# Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:
# Suppose this list is answer = [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
# Return the list answer. If there multiple valid answers, return any of them.
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n - k + 1))
        for i in range(k):
            if i % 2 == 0:
                res.append(n - i // 2)
            else:
                res.append(n - k + (i + 1) // 2)
        return res
 
