# Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.
# Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible.
# Students must be placed in seats in good condition.
from typing import List
from functools import cache


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        self.n = len(seats[0])
        self.available_seat_masks = [self.get_seat_mask(row) for row in seats]
        return self.search(self.available_seat_masks[0], 0)

    def get_seat_mask(self, seat):
        mask = 0
        for i, c in enumerate(seat):
            if c == ".":
                mask |= 1 << i
        return mask

    @cache
    def search(self, current_seat_mask, i):
        ans = 0
        for mask in range(1 << self.n):
            if (current_seat_mask | mask) != current_seat_mask or (mask & (mask << 1)):
                continue
            cnt = bin(mask).count("1")
            if i == len(self.available_seat_masks) - 1:
                ans = max(ans, cnt)
            else:
                next_seat_mask = self.available_seat_masks[i + 1]
                next_seat_mask &= ~(mask << 1)
                next_seat_mask &= ~(mask >> 1)
                ans = max(ans, cnt + self.search(next_seat_mask, i + 1))
        return ans
