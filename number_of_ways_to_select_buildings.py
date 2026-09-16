# You are given a 0-indexed binary string s which represents the types of buildings along a street where:
# s[i] = '0' denotes that the ith building is an office and
# s[i] = '1' denotes that the ith building is a restaurant.
# As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.
# Return the number of valid ways to select 3 buildings.
class Solution:
    def numberOfWays(self, s: str) -> int:
        n0 = [0 for i in range(len(s))]
        n1 = [0 for i in range(len(s))]
        n01 = [0 for i in range(len(s))]
        n10 = [0 for i in range(len(s))]
        n101 = [0 for i in range(len(s))]
        n010 = [0 for i in range(len(s))]
        for i in range(len(s)):
            if i > 0:
                if s[i] == "0":
                    n0[i] = n0[i - 1] + 1
                    n1[i] = n1[i - 1]
                    n01[i] = n01[i - 1]
                    n10[i] = n10[i - 1] + n1[i - 1]
                    n101[i] = n101[i - 1]
                    n010[i] = n010[i - 1] + n01[i - 1]
                else:
                    n0[i] = n0[i - 1]
                    n1[i] = n1[i - 1] + 1
                    n01[i] = n01[i - 1] + n0[i - 1]
                    n10[i] = n10[i - 1]
                    n101[i] = n101[i - 1] + n10[i - 1]
                    n010[i] = n010[i - 1]
            else:
                if s[i] == "0":
                    n0[i] = 1
                else:
                    n1[i] = 1
        return n010[-1] + n101[-1]
