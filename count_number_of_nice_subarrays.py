# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        count_cur = 0
        odd_numbers = {0: 1}
        for num in nums:
            if num % 2 == 1:
                count_cur += 1
            if count_cur-k in odd_numbers:
                count += odd_numbers[count_cur-k]
            if count_cur in odd_numbers:
                odd_numbers[count_cur] += 1
            else:
                odd_numbers[count_cur] = 1
        return count
