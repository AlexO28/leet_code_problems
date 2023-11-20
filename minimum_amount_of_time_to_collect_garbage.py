# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.
# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.
# There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.
# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.
# Return the minimum number of minutes needed to pick up all the garbage.

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbage_M = 0
        garbage_P = 0
        garbage_G = 0
        for elem in garbage[0]:
            if elem == "M":
                garbage_M += 1
            elif elem == "P":
                garbage_P += 1
            else:
                garbage_G += 1
        prev_M = 0
        prev_P = 0
        prev_G = 0
        for j in range(len(travel)):
            has_M = False
            has_P = False
            has_G = False
            for elem in garbage[j+1]:
                if elem == "M":
                    garbage_M += 1
                    has_M = True
                elif elem == "P":
                    garbage_P += 1
                    has_P = True
                else:
                    garbage_G += 1
                    has_G = True
            if has_M:
                garbage_M += sum(travel[prev_M:(j+1)])
                prev_M = j+1
            if has_P:
                garbage_P += sum(travel[prev_P:(j+1)])
                prev_P = j+1
            if has_G:
                garbage_G += sum(travel[prev_G:(j+1)])
                prev_G = j+1
        return garbage_M + garbage_P + garbage_G 
