# You are given two strings current and correct representing two 24-hour times.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.
# Return the minimum number of operations needed to convert current to correct.
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_hour, cur_minutes = current.split(":")
        current = int(cur_hour) * 60 + int(cur_minutes)
        correct_hour, correct_minutes = correct.split(":")
        correct = int(correct_hour) * 60 + int(correct_minutes)
        if current > correct:
            correct += 24 * 60
        correct -= current
        min_operations, remainder = divmod(correct, 60)
        main_part, remainder = divmod(remainder, 15)
        min_operations += main_part
        main_part, remainder = divmod(remainder, 5)
        return min_operations + main_part + remainder
