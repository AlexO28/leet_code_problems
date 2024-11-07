# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        start = 0
        end = len(s)
        for elem in list(s):
            if elem == "I":
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1
        res.append(start)
        return res
