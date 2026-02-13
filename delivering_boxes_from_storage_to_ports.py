# You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a limit on the number of boxes and the total weight that it can carry.
# You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three integers portsCount, maxBoxes, and maxWeight.
# ports​​i is the port where you need to deliver the ith box and weightsi is the weight of the ith box.
# portsCount is the number of ports.
# maxBoxes and maxWeight are the respective box and weight limits of the ship.
# The boxes need to be delivered in the order they are given. The ship will follow these steps:
# The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and maxWeight constraints.
# For each loaded box in order, the ship will make a trip to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no trip is needed, and the box can immediately be delivered.
# The ship then makes a return trip to storage to take more boxes from the queue.
# The ship must end at storage after all the boxes have been delivered.
# Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.
from typing import List
from collections import deque
from itertools import accumulate, pairwise


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        ws = list(accumulate((box[1] for box in boxes), initial=0))
        c = [int(a != b) for a, b in pairwise(box[0] for box in boxes)]
        cs = list(accumulate(c, initial=0))
        f = [0] * (len(boxes) + 1)
        q = deque([0])
        for i in range(1, len(boxes) + 1):
            while q and (i - q[0] > maxBoxes or ws[i] - ws[q[0]] > maxWeight):
                q.popleft()
            if q:
                f[i] = cs[i - 1] + f[q[0]] - cs[q[0]] + 2
            if i < len(boxes):
                while q and f[q[-1]] - cs[q[-1]] >= f[i] - cs[i]:
                    q.pop()
                q.append(i)
        return f[-1]
