# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.
# Return a sorted list of the items such that:
# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty list if there is no solution.
from typing import List
from collections import deque


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        index = m
        group_to_items = [[] for i in range(n + m)]
        for item, grp in enumerate(group):
            if grp == -1:
                group[item] = index
                index += 1
            group_to_items[group[item]].append(item)
        item_degree = [0] * n
        group_degree = [0] * (n + m)
        item_graph = [[] for i in range(n)]
        group_graph = [[] for i in range(n + m)]      
        for i, gi in enumerate(group):
            for j in beforeItems[i]:
                gj = group[j]
                if gi == gj:
                    item_degree[i] += 1
                    item_graph[j].append(i)
                else:
                    if gi not in group_graph[gj]:
                        group_degree[gi] += 1
                        group_graph[gj].append(gi)
        group_order = self.topological_sort(group_degree, group_graph, list(range(n + m)))
        if not group_order:
            return []      
        final_order = []
        for group_index in group_order:
            items_in_group = group_to_items[group_index]
            item_order = self.topological_sort(item_degree, item_graph, items_in_group)
            if len(items_in_group) != len(item_order):
                return []
            final_order.extend(item_order)
        return final_order
        

    def topological_sort(self, degrees, graph, items):
        queue = deque([item for item in items if degrees[item] == 0])
        result = []
        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in graph[current]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
        return result if len(result) == len(items) else []
