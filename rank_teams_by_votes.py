# In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.
from typing import List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        vote_counts = defaultdict(lambda: [0] * (len(votes[0])))
        for vote in votes:
            for position, team in enumerate(vote):
                vote_counts[team][position] += 1
        return "".join(
            sorted(
                vote_counts.keys(),
                key=lambda team: (vote_counts[team], -ord(team)),
                reverse=True,
            )
        )
