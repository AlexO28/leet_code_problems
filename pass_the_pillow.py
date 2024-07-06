# There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.
# Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        main_part, remainder = divmod(time, n-1)
        if main_part % 2 == 0:
            return remainder + 1
        else:
            return n - remainder
