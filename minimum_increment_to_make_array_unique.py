# You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
# Return the minimum number of moves to make every value in nums unique.
import bisect


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        keys = list(freq_dict.keys())
        keys.sort()
        res = 0
        counter = 0
        ind = 0
        pos = keys[0]
        while counter < len(nums):
            val = freq_dict[pos]
            if val > 1:
                res += val - 1
                freq_dict[pos] = 1
                pos += 1
                if pos in freq_dict.keys():
                    freq_dict[pos] += val - 1
                    ind += 1
                else:
                    freq_dict[pos] = val - 1
                    bisect.insort(keys, pos)
                    ind += 1
            else:
                ind += 1
                if ind == len(keys):
                    break
                else:
                    pos = keys[ind]
            counter += 1
        return res
