# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
# Return the maximum total number of units that can be put on the truck.
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse = True)
        ind = 0
        res = 0
        while truckSize > 0:
            if ind == len(boxTypes):
                break
            if boxTypes[ind][0] > 0:
                boxTypes[ind][0] -= 1
                res += boxTypes[ind][1]
                truckSize -= 1
            else:
                ind += 1
        return res
