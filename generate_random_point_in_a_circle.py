# Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform random point inside the circle.
# Implement the Solution class:
# Solution(double radius, double x_center, double y_center) initializes the object with the radius of the circle radius and the position of the center (x_center, y_center).
# randPoint() returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array [x, y].
import math
import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.radius = radius
        
    def randPoint(self) -> List[float]:
        r = ((random.random()) ** 0.5)*self.radius
        phi = random.random()*2*math.pi
        return [self.x + r*math.cos(phi), self.y + r*math.sin(phi)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
