# There are n people and 40 types of hats labeled from 1 to 40.
# Given a 2D integer array hats, where hats[i] is a list of all hats preferred by the ith person.
# Return the number of ways that n people can wear different hats from each other.
# Since the answer may be too large, return it modulo 109 + 7.
from typing import List
from collections import defaultdict


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        hat_to_people = defaultdict(list)
        for person_id, person_hats in enumerate(hats):
            for hat in person_hats:
                hat_to_people[hat].append(person_id)
        MOD = 10**9 + 7
        max_hat_id = max(max(person_hats) for person_hats in hats)
        dp = [[0] * (1 << len(hats)) for i in range(max_hat_id + 1)]
        dp[0][0] = 1
        for hat_id in range(1, max_hat_id + 1):
            for people_mask in range(1 << len(hats)):
                dp[hat_id][people_mask] = dp[hat_id - 1][people_mask]
                for person in hat_to_people[hat_id]:
                    if people_mask >> person & 1:
                        previous_mask = people_mask ^ (1 << person)
                        dp[hat_id][people_mask] = (
                            dp[hat_id][people_mask] + dp[hat_id - 1][previous_mask]
                        ) % MOD
        return dp[max_hat_id][(1 << len(hats)) - 1]
