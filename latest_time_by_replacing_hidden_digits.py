# You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).
# The valid times are those inclusively between 00:00 and 23:59.
# Return the latest valid time you can get from time by replacing the hidden digits.
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        first_val = time[0]
        second_val = time[1]
        third_val = time[3]
        fourth_val = time[4]
        if first_val == "?":
            if second_val in ["?", "0", "1", "2", "3"]:
                first_val = "2"
            else:
                first_val = "1"
        if second_val == "?":
            if first_val == "2":
                second_val = "3"
            else:
                second_val = "9"
        if third_val == "?":
            third_val = "5"
        if fourth_val == "?":
            fourth_val = "9"
        return first_val + second_val + ":" + third_val + fourth_val
