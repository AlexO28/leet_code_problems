# You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].
# For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.
# Implement the TopVotedCandidate class:
# TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
# int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
from collections import Counter


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        max_votes = 0
        current_leader = 0
        vote_counts = Counter()
        self.times = times
        self.leaders = []
        for j in range(len(persons)):
            vote_counts[persons[j]] += 1
            if vote_counts[persons[j]] >= max_votes:
                max_votes = vote_counts[persons[j]]
                current_leader = persons[j]
            self.leaders.append(current_leader)


    def q(self, t: int) -> int:
        left = 0
        right = len(self.leaders) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.leaders[left]
