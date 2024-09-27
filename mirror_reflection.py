# There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.
# The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.
# Given the two integers p and q, return the number of the receptor that the ray meets first.
# The test cases are guaranteed so that the ray will meet a receptor eventually.
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while True:
            main_part_p, remainder_p = divmod(p, 2)
            main_part_q, remainder_q = divmod(q, 2)
            if (remainder_p == 0) and (remainder_q == 0):
                p = main_part_p
                q = main_part_q
            else:
                break
        if remainder_p == 0:
            return 2
        elif remainder_q == 0:
            return 0
        else:
            return 1
