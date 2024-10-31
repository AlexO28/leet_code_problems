# Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
# A subarray is a contiguous non-empty sequence of elements within an array.
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        prev = 0
        for j in range(len(arr)):
            prev |= arr[j]
            cur = 0
            for i in range(j, -1, -1):
                cur |= arr[i]
                res.add(cur)
                if cur == prev:
                    break
        return len(res)
