# A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.
# For example, these are arithmetic sequences:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic:
# 1, 1, 2, 5, 7
# You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.
# Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for j in range(len(l)):
            seq = nums[l[j]:(r[j]+1)]
            seq.sort()
            if len(seq) <= 1:
                res.append(False)
            elif len(seq) == 2:
                res.append(True)
            else:
                diff = seq[1] - seq[0]
                cycle_res = True
                for i in range(2, len(seq)):
                    if seq[i] - seq[i-1] != diff:
                        cycle_res = False
                        break
                res.append(cycle_res)
        return res
