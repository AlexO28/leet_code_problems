# In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.
# Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.
# Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.
# It is guaranteed an answer exists.
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_index = {req_skills[index]: index for index in range(len(req_skills))}
        people_skills = [0] * (len(people))
        for i in range(len(people)):
            for skill in people[i]:
                people_skills[i] |= 1 << skill_to_index[skill]
        min_team_size = [61] * (1 << len(req_skills))
        last_added_person = [0] * (1 << len(req_skills))
        prev_skill_set = [0] * (1 << len(req_skills))
        min_team_size[0] = 0
        for skill_set in range(1 << len(req_skills)):
            if min_team_size[skill_set] <= 60:
                for j in range(len(people)):
                    new_skill_set = skill_set | people_skills[j]
                    if min_team_size[skill_set] + 1 < min_team_size[new_skill_set]:
                        min_team_size[new_skill_set] = min_team_size[skill_set] + 1
                        last_added_person[new_skill_set] = j
                        prev_skill_set[new_skill_set] = skill_set
        current_skill_set = (1 << len(req_skills)) - 1
        team_indices = []
        while current_skill_set > 0:
            team_indices.append(last_added_person[current_skill_set])
            current_skill_set = prev_skill_set[current_skill_set]
        return team_indices
