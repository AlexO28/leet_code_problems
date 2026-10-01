# You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.
# You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:
# Trim each number in nums to its rightmost trimi digits.
# Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
# Reset each number in nums to its original length.
# Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.
# Note:
# To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.
# Strings in nums may contain leading zeros.
class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        res = []
        for query in queries:
            nums_new = []
            for elem in nums:
                elem_str = str(elem)
                if len(elem_str) <= query[1]:
                    nums_new.append(elem_str)
                else:
                    nums_new.append(elem_str[-query[1]:])
            res.append(sorted(range(len(nums_new)), key=lambda i: nums_new[i])[query[0] - 1])
        return res
