# You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.
# You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.
# Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean*(n + len(rolls)) - sum(rolls)
        main_part, remainder = divmod(total, n)
        if (main_part > 6) or ((main_part == 6) and (remainder > 0)) or (main_part <= 0):
            return []
        else:
            res = [main_part]*n
            if remainder > 0:
                for j in range(remainder):
                    res[j] += 1
            return res
