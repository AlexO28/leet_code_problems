# You are given an integer n.
# Each number from 1 to n is grouped according to the sum of its digits.
# Return the number of groups that have the largest size.
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = []
        for i in range(1, n + 1):
            groups.append(sum([int(elem) for elem in list(str(i))]))
        freq_dict = {}
        for group in groups:
            if group in freq_dict:
                freq_dict[group] += 1
            else:
                freq_dict[group] = 1
        nums = list(freq_dict.values())
        nums.sort()
        max_val = nums[-1]
        res = 0
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == max_val:
                res += 1
            else:
                break
        return res
