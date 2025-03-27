# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:
# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cur_dir = "N"
        pos = [0, 0]
        for letter in list(instructions):
            if letter == "G":
                unit_vector = self.get_unit_vector(cur_dir)
                pos[0] += unit_vector[0]
                pos[1] += unit_vector[1]
            elif letter == "L":
                if cur_dir == "N":
                    cur_dir = "W"
                elif cur_dir == "W":
                    cur_dir = "S"
                elif cur_dir == "S":
                    cur_dir = "E"
                else:
                    cur_dir = "N"
            else:
                if cur_dir == "N":
                    cur_dir = "E"
                elif cur_dir == "E":
                    cur_dir = "S"
                elif cur_dir == "S":
                    cur_dir = "W"
                else:
                    cur_dir = "N"
        return (pos == [0, 0]) or (cur_dir != "N")


    def get_unit_vector(self, cur_dir):
        if cur_dir == "N":
            return [0, 1]
        elif cur_dir == "S":
            return [0, -1]
        elif cur_dir == "W":
            return [-1, 0]
        else:
            return [1, 0]
