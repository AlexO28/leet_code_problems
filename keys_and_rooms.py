# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        to_visit = [0]
        while len(to_visit) > 0:
            new_visits = {}
            for room in to_visit:
                visited[room] = 1
                if len(rooms[room]) > 0:
                    for new_room in rooms[room]:
                        if new_room not in visited:
                            if new_room not in new_visits:
                                new_visits[new_room] = 1
            to_visit = list(new_visits.keys()).copy()
        return len(visited) == len(rooms)
