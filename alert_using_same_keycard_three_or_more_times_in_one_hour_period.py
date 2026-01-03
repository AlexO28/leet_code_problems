# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        workers_info = {}
        for j in range(len(keyName)):
            if keyName[j] in workers_info:
                workers_info[keyName[j]].append(keyTime[j])
            else:
                workers_info[keyName[j]] = [keyTime[j]]
        res = []
        for worker in workers_info:
            if len(workers_info[worker]) > 2:
                times = [self.time_to_number(info) for info in workers_info[worker]]
                times.sort()
                for j in range(len(times) - 2):
                    if ((times[j + 1] - times[j]) <= 60) and (
                        (times[j + 2] - times[j]) <= 60
                    ):
                        res.append(worker)
                        break
        res.sort()
        return res

    def time_to_number(self, line):
        hour, minute = line.split(":")
        return int(hour) * 60 + int(minute)
