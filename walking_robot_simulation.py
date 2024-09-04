# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
# Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [0, 1]
        position = [0, 0]
        max_dist = 0
        obstacles_dict = {}
        for obstacle in obstacles:
            obstacles_dict[str(obstacle[0]) + "_" + str(obstacle[1])] = 1
        for command in commands:
            if command > 0:
                for j in range(1, command+1):
                    next_position = [position[0] + direction[0], position[1] + direction[1]]
                    if str(next_position[0]) + "_" + str(next_position[1]) in obstacles_dict:
                        break
                    position = next_position
                max_dist = max(max_dist, position[0] ** 2 + position[1] ** 2)
            else:
                if command == -2:
                    if direction == [0, 1]:
                        direction = [-1, 0]
                    elif direction == [-1, 0]:
                        direction = [0, -1]
                    elif direction == [0, -1]:
                        direction = [1, 0]
                    else:
                        direction = [0, 1]
                else:
                    if direction == [0, 1]:
                        direction = [1, 0]
                    elif direction == [1, 0]:
                        direction = [0, -1]
                    elif direction == [0, -1]:
                        direction = [-1, 0]
                    else:
                        direction = [0, 1]
        return max_dist
