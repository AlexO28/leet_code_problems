# You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".
# In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.
# Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.
class Solution:
    def countTime(self, time: str) -> int:
        cur_hour, cur_minute = time.split(":")
        res = 0
        for hour in range(24):
            for minute in range(60):
                hour_str = str(hour)
                if len(hour_str) == 1:
                    hour_str = "0" + hour_str
                minute_str = str(minute)
                if len(minute_str) == 1:
                    minute_str = "0" + minute_str
                if (cur_hour[0] != "?") and (cur_hour[0] != hour_str[0]):
                    continue 
                if (cur_hour[1] != "?") and (cur_hour[1] != hour_str[1]):
                    continue
                if (cur_minute[0] != "?") and (cur_minute[0] != minute_str[0]):
                    continue
                if (cur_minute[1] != "?") and (cur_minute[1] != minute_str[1]):
                    continue
                res += 1
        return res
