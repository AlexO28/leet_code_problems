# You have n dice, and each dice has k faces numbered from 1 to k.
# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        ways_to_achieve_sum = [1] + [0] * target
        MOD = 10 ** 9 + 7
        for i in range(1, n + 1):
            current_ways = [0] * (target + 1)
            for sum_value in range(1, min(i * k, target) + 1):
                for face_value in range(1, min(sum_value, k) + 1):
                    current_ways[sum_value] = (current_ways[sum_value] + ways_to_achieve_sum[sum_value - face_value]) % MOD
            ways_to_achieve_sum = current_ways
        return ways_to_achieve_sum[target]
