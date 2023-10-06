# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num not in freq_dict.keys():
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        arr = list(freq_dict.values())
        arr.sort(reverse=True)
        key_values = arr[:(k)]
        arr = []
        for key in freq_dict.keys():
            if freq_dict[key] in key_values:
                arr.append(key)
        return arr
