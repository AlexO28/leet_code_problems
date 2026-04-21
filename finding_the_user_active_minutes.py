# You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.
# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.
# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.
# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.
Return the array answer as described above.
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_info = {}
        for log in logs:
            if log[0] in user_info:
                user_info[log[0]].append(log[1])
            else:
                user_info[log[0]] = [log[1]]
        inverse_dict = {}
        for user in user_info:
            duration = len(set(user_info[user]))
            if duration in inverse_dict:
                inverse_dict[duration] += 1
            else:
                inverse_dict[duration] = 1
        res = []
        for j in range(1, k + 1):
            if j in inverse_dict:
                res.append(inverse_dict[j])
            else:
                res.append(0)
        return res
