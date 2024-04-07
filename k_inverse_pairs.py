# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
# Given two integers n and k, return the number of different arrays consisting of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * k        
        prefix_sum = [0] * (k + 2)      
        for current_number in range(1, n + 1):
            for inverse_count in range(1, k + 1):
                dp[inverse_count] = (prefix_sum[inverse_count + 1] - 
                                     prefix_sum[max(0, inverse_count - (current_number - 1))]) % mod          
            for index in range(1, k + 2):
                prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod              
        return dp[k]
 
