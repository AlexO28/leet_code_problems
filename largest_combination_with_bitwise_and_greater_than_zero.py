# The bitwise AND of an array nums is the bitwise AND of all integers in nums.
# Also, for nums = [7], the bitwise AND is 7.
# You are given an array of positive integers candidates. Compute the bitwise AND for all possible combinations of elements in the candidates array.
# Return the size of the largest combination of candidates with a bitwise AND greater than 0.
class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        new_candidates = []
        max_len = 0
        for candidate in candidates:
            new_candidate = bin(candidate)[2:]
            new_candidates.append(new_candidate[::-1])
            max_len = max(max_len, len(new_candidate))
        largest = 0
        for i in range(max_len):
            cur_largest = 0
            for candidate in new_candidates:
                if len(candidate) >= i + 1:
                    if candidate[i] == "1":
                        cur_largest += 1
            largest = max(largest, cur_largest)
        return largest
