# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
# Answers within 10-5 of the actual value will be accepted as correct.
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        if minutes <= 30:
            angle_min = (minutes / 30) * 180
            side_left_min = True
        else:
            angle_min = ((60 - minutes) / 30) * 180
            side_left_min = False
        hour = ((60 - minutes) * hour + minutes * (hour + 1)) / 60
        if hour <= 6:
            angle_hour = (hour / 6) * 180
            side_left_hour = True
        else:
            angle_hour = ((12 - hour) / 6) * 180
            side_left_hour = False
        if (side_left_min and side_left_hour) or (
            not side_left_min and not side_left_hour
        ):
            return abs(angle_min - angle_hour)
        else:
            return min(
                abs(angle_min - (360 - angle_hour)),
                abs(angle_hour - (360 - angle_min)),
                (angle_hour + angle_min),
            )
