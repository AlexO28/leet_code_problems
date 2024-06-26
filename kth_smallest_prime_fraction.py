# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        frac_dict = {}
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                val = arr[i]/arr[j]
                frac_dict[val] = [i, j]
        keys = list(frac_dict.keys())
        keys.sort()
        i, j = frac_dict[keys[k-1]]
        return arr[i], arr[j]
