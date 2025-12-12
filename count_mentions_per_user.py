# You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.
# Each events[i] can be either of the following two types:
# Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
# This event indicates that a set of users was mentioned in a message at timestampi.
# The mentions_stringi string can contain one of the following tokens:
# id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
# ALL: mentions all users.
# HERE: mentions all online users.
# Offline Event: ["OFFLINE", "timestampi", "idi"]
# This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
# Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.
# All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.
# Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        here_timestamps = []
        offlines = []
        for j in range(numberOfUsers):
            offlines.append([])
        for message, timestamp, mentions_string in events:
            if message == "MESSAGE":
                if mentions_string == "HERE":
                    here_timestamps.append(int(timestamp))
                elif mentions_string == "ALL":
                    for j in range(len(mentions)):
                        mentions[j] += 1
                else:
                    ids = mentions_string.split(" ")
                    for id in ids:
                        mentions[int(id.replace("id", ""))] += 1
            else:
                id = int(mentions_string.replace("id", ""))
                timestamp = int(timestamp)
                offlines[id].append([timestamp, timestamp + 60])
        for timestamp in here_timestamps:
            for id in range(len(offlines)):
                if len(offlines[id]) == 0:
                    mentions[id] += 1
                else:
                    found = False
                    for interval in offlines[id]:
                        if interval[0] <= timestamp < interval[1]:
                            found = True
                            break
                    if not found:
                        mentions[id] += 1
        return mentions
