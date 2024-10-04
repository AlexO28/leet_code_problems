# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.
# The chemistry of a team is equal to the product of the skills of the players on that team.
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        skill.sort()
        total_skill = skill[0] + skill[-1]
        total_chemistry = skill[0] * skill[-1]
        for j in range(1, len(skill)//2):
            if skill[j] + skill[len(skill)-j-1] != total_skill:
                return -1
            total_chemistry += skill[j] * skill[len(skill)-j-1]
        return total_chemistry
