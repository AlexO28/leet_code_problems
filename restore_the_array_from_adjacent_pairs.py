# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        nums_dict = {}
        for pair in adjacentPairs:
            if pair[0] in nums_dict.keys():
                nums_dict[pair[0]].append(pair[1])
            else:
                nums_dict[pair[0]] = [pair[1]]
            if pair[1] in nums_dict.keys():
                nums_dict[pair[1]].append(pair[0])
            else:
                nums_dict[pair[1]] = [pair[0]]
        for i in nums_dict.keys():
            if len(nums_dict[i]) == 1:
                val = i
                break
        nums = [val]
        while len(nums) <= len(adjacentPairs) + 1:
            next_val = nums_dict[val][0]
            nums_dict[next_val].remove(val)
            nums.append(next_val)
            val = next_val
            if len(nums_dict[val]) == 0:
                break
        return nums
