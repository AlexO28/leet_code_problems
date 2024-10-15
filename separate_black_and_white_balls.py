# There are n balls on a table, each ball has a color black or white.
# You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
# In each step, you can choose two adjacent balls and swap them.
# Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.
class Solution:
    def minimumSteps(self, s: str) -> int:
        cur_counter = 0
        res_counter = 0
        for j in range(len(s)-1, -1, -1):
            if s[j] == "0":
                cur_counter += 1
            else:
                res_counter += cur_counter
        return res_counter
