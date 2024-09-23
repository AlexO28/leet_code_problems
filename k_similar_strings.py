# Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.
# Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.
from collections import deque


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        self.s1 = s1
        self.s2 = s2
        queue = deque([s1])
        visited = set([s1])
        number_of_swaps = 0
        while True:
            queue_length = len(queue)
            for j in range(queue_length):
                current_string = queue.popleft()
                if current_string == s2:
                    return number_of_swaps
                else:
                    for next_state in self.generate_next_states(current_string):
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append(next_state)
            number_of_swaps += 1


    def generate_next_states(self, current_string):
        i = 0
        while current_string[i] == self.s2[i]:
            i += 1
        next_states = []
        for j in range(i+1, len(self.s1)):
            if (current_string[j] == self.s2[i]) and (current_string[j] != self.s2[j]):
                next_states.append(current_string[:i] + current_string[j] + current_string[i+1:j] + current_string[i] + current_string[j+1:])
        return next_states
