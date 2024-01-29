# Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.
# Every house can be warmed, as long as the house is within the heater's warm radius range. 
# Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.
# Notice that all the heaters follow your radius standard, and the warm radius will the same.
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        j = 0
        for house in houses:
            while (j+1 < len(heaters)) and (house - heaters[j] > heaters[j + 1] - house):
                j += 1
            res = max(res, abs(heaters[j] - house))
        return res
