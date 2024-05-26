# You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.
# Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.
# Implement the Solution class:
# Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
# int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.
import random


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.mapping_range_limit = n - len(blacklist) 
        self.mapping_dict = {}
        blacklist_set = set(blacklist)
        mapping_start_index = self.mapping_range_limit
        for black_number in blacklist:
            if black_number < self.mapping_range_limit:
                while mapping_start_index in blacklist_set:
                    mapping_start_index += 1
                self.mapping_dict[black_number] = mapping_start_index
                mapping_start_index += 1

    def pick(self) -> int:
        random_pick = random.randrange(self.mapping_range_limit)
        return self.mapping_dict.get(random_pick, random_pick)        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
