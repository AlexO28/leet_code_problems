# A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".
# The robot can be instructed to move for a specific number of steps. For each step, it does the following.
# Attempts to move forward one cell in the direction it is facing
# If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
# After the robot finishes moving the number of steps required, it stops and awaits the next instruction.
# Implement the Robot class:
# Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
# void step(int num) Instructs the robot to move forward num steps.
# int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
# String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.max_len = 2 * (width + height - 2)
        self.positions = [i for i in range(self.max_len)]
        self.cur_pos = 0
        self.did_not_move = True

    def step(self, num: int) -> None:
        self.did_not_move = False
        self.cur_pos = (self.cur_pos + num) % self.max_len

    def getPos(self) -> List[int]:
        if self.cur_pos < self.width - 1:
            return [self.cur_pos, 0]
        curpos = self.cur_pos - self.width + 1
        if curpos < self.height - 1:
            return [self.width - 1, curpos]
        curpos -= self.height - 1
        if curpos < self.width - 1:
            return [self.width - curpos - 1, self.height - 1]
        curpos -= self.width - 1
        return [0, self.height - curpos - 1]

    def getDir(self) -> str:
        x, y = self.getPos()
        if self.did_not_move:
            return "East"
        elif (x == 0) and (y == 0):
            return "South"
        elif y == 0:
            return "East"
        elif x == self.width - 1:
            return "North"
        elif y == self.height - 1:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
