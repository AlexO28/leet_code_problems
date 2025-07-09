# You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:
# status[i] is 1 if the ith box is open and 0 if the ith box is closed,
# candies[i] is the number of candies in the ith box,
# keys[i] is a list of the labels of the boxes you can open after opening the ith box.
# containedBoxes[i] is a list of the boxes you found inside the ith box.
# You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
# Return the maximum number of candies you can get following the rules above.
from typing import List
from collections import deque


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        queue = deque([box for box in initialBoxes if status[box] == 1])
        total_candies = sum(candies[box] for box in initialBoxes if status[box] == 1)
        boxes_in_hand = set(initialBoxes)
        boxes_accessed = {box for box in initialBoxes if status[box] == 1}
        while queue:
            current_box = queue.popleft()
            for key in keys[current_box]:
                status[key] = 1
                if (key in boxes_in_hand) and (key not in boxes_accessed):
                    total_candies += candies[key]
                    boxes_accessed.add(key)
                    queue.append(key)
            for box_id in containedBoxes[current_box]:
                boxes_in_hand.add(box_id)
                if status[box_id] and box_id not in boxes_accessed:
                    total_candies += candies[box_id]
                    boxes_accessed.add(box_id)
                    queue.append(box_id)
        return total_candies
