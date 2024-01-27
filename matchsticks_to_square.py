# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
# Return true if you can make this square and false otherwise.
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        target, rel = divmod(sum(matchsticks), 4)
        if rel > 0:
            return False
        matchsticks.sort(reverse=True)
        return self.dfs(0, [0, 0, 0, 0], target, matchsticks)
        
    def dfs(self, start_index, sides, side_length, matchsticks):
        if start_index == len(matchsticks):
            return (side_length == sides[0]) and\
                   (side_length == sides[1]) and\
                   (side_length == sides[2]) and\
                   (side_length == sides[3])
        for j in range(4):
            if sides[j] + matchsticks[start_index] <= side_length:
                sides[j] += matchsticks[start_index]
                if self.dfs(start_index + 1, sides, side_length, matchsticks):
                    return True
                sides[j] -= matchsticks[start_index]
        return False
