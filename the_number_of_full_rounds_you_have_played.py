# You are participating in an online chess tournament. There is a chess round that starts every 15 minutes. The first round of the day starts at 00:00, and after every 15 minutes, a new round starts.
# For example, the second round starts at 00:15, the fourth round starts at 00:45, and the seventh round starts at 01:30.
# You are given two strings loginTime and logoutTime where:
# loginTime is the time you will login to the game, and
# logoutTime is the time you will logout from the game.
# If logoutTime is earlier than loginTime, this means you have played from loginTime to midnight and from midnight to logoutTime.
# Return the number of full chess rounds you have played in the tournament.
# Note: All the given times follow the 24-hour clock. That means the first round of the day starts at 00:00 and the last round of the day starts at 23:45.
import numpy as np


class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        loginTime = self.timeToNumber(loginTime)
        logoutTime = self.timeToNumber(logoutTime)
        if loginTime > logoutTime:
            logoutTime += 1440
        loginTime = int(np.ceil(loginTime / 15))
        logoutTime = int(np.floor(logoutTime / 15))
        return max(logoutTime - loginTime, 0)

    def timeToNumber(selff, time):
        hour, minute = time.split(":")
        return int(hour) * 60 + int(minute)
