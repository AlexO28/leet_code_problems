# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        rev_freq_dict = {}
        for key in freq_dict:
            if freq_dict[key] in rev_freq_dict:
                rev_freq_dict[freq_dict[key]].append(key)
            else:
                rev_freq_dict[freq_dict[key]] = [key]
        freqs = list(rev_freq_dict.keys())
        freqs.sort()
        res = []
        for freq in freqs:
            temp = rev_freq_dict[freq] * freq
            temp.sort(reverse=True)
            res.extend(temp)
        return res
