# Given an array of integers arr.
# We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        res = 0
        for i in range(len(arr)-1):
            cur_res = arr[i]
            for j in range(i+1, len(arr)):
                cur_res ^= arr[j]
                if cur_res == 0:
                    res += j-i
        return res
