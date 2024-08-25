# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        if len(routes) == 1:
            if (source in routes[0]) and (target in routes[0]):
                return 1
            else:
                return -1
        crossroads = [{} for i in range(len(routes))]
        routes_in_dict = [{} for i in range(len(routes))]
        for j in range(len(routes)):
            for elem in routes[j]:
                routes_in_dict[j][elem] = 1
        for j in range(len(routes)):
            for stop in routes_in_dict[j]:
                for i in range(len(routes)):
                    if i != j:
                        if i not in crossroads[j]:
                            if stop in routes_in_dict[i]:
                                crossroads[j][i] = 1
        lines_to_visit = []
        for j in range(len(routes)):
            if source in routes[j]:
                lines_to_visit.append(j)
        if len(lines_to_visit) == 0:
            return -1
        number_of_lines = 1
        lines_visited = []
        while len(lines_to_visit) > 0:
            for line in lines_to_visit:
                if target in routes[line]:
                    return number_of_lines
            number_of_lines += 1
            lines_visited.extend(lines_to_visit.copy())
            new_lines_to_visit = []
            for line in lines_to_visit:
                for elem in crossroads[line]:
                    if (elem not in new_lines_to_visit) and (elem not in lines_visited):
                        new_lines_to_visit.append(elem)
            lines_to_visit = new_lines_to_visit
        return -1
