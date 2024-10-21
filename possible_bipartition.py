# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        connections = {}
        for dislike in dislikes:
            if dislike[0]-1 in connections:
                connections[dislike[0]-1].append(dislike[1]-1)
            else:
                connections[dislike[0]-1] = [dislike[1]-1]
            if dislike[1]-1 in connections:
                connections[dislike[1]-1].append(dislike[0]-1)
            else:
                connections[dislike[1]-1] = [dislike[0]-1]
        self.parent = list(range(n))
        for person in range(n):
            if person not in connections:
                continue
            for other_person in connections[person]:
                if self.find_root(person) == self.find_root(other_person):
                    return False
                else:
                    self.parent[self.find_root(other_person)] = self.find_root(connections[person][0])
        return True


    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]
