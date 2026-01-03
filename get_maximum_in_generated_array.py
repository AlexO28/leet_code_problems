# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums​​​.
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            res = [0, 1]
            for j in range(2, n + 1):
                main_part, remainder = divmod(j, 2)
                if remainder == 0:
                    res.append(res[main_part])
                else:
                    res.append(res[main_part] + res[main_part + 1])
            return max(res)
