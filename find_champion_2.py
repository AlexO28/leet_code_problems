# There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.
# You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.
# A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.
# Team a will be the champion of the tournament if there is no team b that is stronger than team a.
# Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weak_teams = set()
        strong_teams = [i for i in range(n)]
        for team1, team2 in edges:
            weak_teams.add(team2)
        strong_teams = [team for team in strong_teams if team not in weak_teams]
        if len(strong_teams) == 1:
            return strong_teams[0]
        else:
            return -1
