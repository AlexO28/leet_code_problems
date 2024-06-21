# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        self.deadend_set = set(deadends)
        if "0000" in self.deadend_set:
            return -1
        self.target = target
        return self.bidirectional_bfs()

    def get_next_states(self, state):
        next_states = []
        state_digits = list(state)
        for i in range(4):
            original_digit = state_digits[i]
            if original_digit == "0":
                state_digits[i] = "9"
            else:
                state_digits[i] = str(int(original_digit) - 1)
            next_states.append(''.join(state_digits))
            if original_digit == "9":
                state_digits[i] = "0"
            else:
                state_digits[i] = str(int(original_digit) + 1)
            next_states.append(''.join(state_digits))
            state_digits[i] = original_digit
        return next_states

    def extend(self, frontier, opposite_frontier, queue):
        for i in range(len(queue)):
            current_state = queue.popleft()
            current_step = frontier[current_state]
            for next_state in self.get_next_states(current_state):
                if next_state in self.deadend_set or next_state in frontier:
                    continue
                if next_state in opposite_frontier:
                    return current_step + 1 + opposite_frontier[next_state]
                frontier[next_state] = current_step + 1
                queue.append(next_state)
        return -1

    def bidirectional_bfs(self):
        start_frontier = {"0000": 0}
        target_frontier = {self.target: 0}
        start_queue = deque(['0000'])
        target_queue = deque([self.target])
        while start_queue and target_queue:
            if len(start_queue) <= len(target_queue):
                result = self.extend(start_frontier, target_frontier, start_queue)
            else:
                result = self.extend(target_frontier, start_frontier, target_queue)
            if result != -1:
                return result
        return -1
