# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        self.bloomDay = bloomDay
        self.k = k
        self.m = m
        while left < right:
            mid = (left + right) // 2
            if self.can_make_bouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def can_make_bouquets(self, day):
        bouquets = 0
        flowers_in_row = 0
        for bloom in self.bloomDay:
            if bloom <= day:
                flowers_in_row += 1
                if flowers_in_row == self.k:
                    bouquets += 1
                    flowers_in_row = 0
            else:
                flowers_in_row = 0
        return bouquets >= self.m
