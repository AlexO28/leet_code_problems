# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_dict = {}
        for num in arr:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        vals = list(freq_dict.values())
        vals.sort()
        res = len(vals)
        ind = 0
        while True:
            if ind >= len(vals):
                return 0
            k -= vals[ind]
            if k < 0:
                return res
            else:
                res -= 1
            ind += 1
