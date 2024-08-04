# You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
# Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(len(nums)):
            summa = 0
            for j in range(i, len(nums)):
                summa += nums[j]
                arr.append(summa)
        arr.sort()
        arr = arr[(left-1):right]
        MOD = 10 ** 9 + 7
        res = 0
        for elem in arr:
            res = (res + elem) % MOD
        return res
