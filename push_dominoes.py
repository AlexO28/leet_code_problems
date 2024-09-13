# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        queue = deque()
        falling_time = [-1]*(len(dominoes))
        forces = {}
        for j in range(len(dominoes)):
            if dominoes[j] != ".":
                queue.append(j)
                falling_time[j] = 0
                if j in forces:
                    forces[j].append(dominoes[j])
                else:
                    forces[j] = [dominoes[j]]
        result = ["."]*(len(dominoes))
        while queue:
            current_id = queue.popleft()
            if len(forces[current_id]) == 1:
                resultant_force = forces[current_id][0]
                result[current_id] = resultant_force
                if resultant_force == 'L':
                    next_id = current_id - 1
                else:
                    next_id = current_id + 1
                if (next_id >= 0) and (next_id < len(dominoes)):
                    current_time = falling_time[current_id]
                    if falling_time[next_id] == -1:
                        queue.append(next_id)
                        falling_time[next_id] = current_time + 1
                        if next_id in forces:
                            forces[next_id].append(resultant_force)
                        else:
                            forces[next_id] = [resultant_force]
                    elif falling_time[next_id] == current_time + 1:
                        forces[next_id].append(resultant_force)
        return ''.join(result)
