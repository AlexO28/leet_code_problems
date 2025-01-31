# You are given a list of songs where the ith song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        song_dict = {}
        for i in range(len(time)):
            dur = time[i] % 60
            if dur in song_dict:
                song_dict[dur] += 1
            else:
                song_dict[dur] = 1
        res = 0
        for dur in song_dict:
            complement_dur = (60 - dur) % 60
            if complement_dur in song_dict:
                if dur == complement_dur:
                    res += song_dict[dur] * (song_dict[dur] - 1) / 2 
                else:
                    res += song_dict[dur] * song_dict[complement_dur] / 2
        return int(res)
