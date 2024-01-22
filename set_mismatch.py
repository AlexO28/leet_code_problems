# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq_dict = {i: 0 for i in range(1, len(nums)+1)}
        for num in nums:
            if num in freq_dict.keys():
                del freq_dict[num]
            else:
                freq_dict[num] = 2
        res = [-1, -1]
        for key in freq_dict.keys():
            if freq_dict[key] == 0:
                res[1] = key
            elif freq_dict[key] == 2:
                res[0] = key
        return res
