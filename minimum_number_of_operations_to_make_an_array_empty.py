# You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
# Choose two elements with equal values and delete them from the array.
# Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        counter = 0
        for key in freq_dict.keys():
            if freq_dict[key] == 1:
                return -1
            else:
                temp = freq_dict[key]
                while True:
                    if (temp == 2) or (temp == 3) or (temp == 0):
                        counter += 1
                        break
                    div, mod = divmod(temp, 3)
                    if mod == 0:
                        counter += div
                        break
                    elif mod == 2:
                        counter += div + 1
                        break
                    temp -= 2
                    counter += 1
        return counter
