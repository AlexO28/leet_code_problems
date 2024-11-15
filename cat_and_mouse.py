# A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
# The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.
# The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.
# During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0).
# Then, the game can end in three ways:
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
# Given a graph, and assuming both players play optimally, return
# 1 if the mouse wins the game,
# 2 if the cat wins the game, or
# 0 if the game is a draw.
from collections import deque


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        self.graph = graph
        result = [[[0] * 2 for i in range(len(graph))] for j in range(len(graph))]
        degrees = [[[0] * 2 for i in range(len(graph))] for j in range(len(graph))]
        for mouse_pos in range(len(graph)):
            for cat_pos in range(1, len(graph)):
                degrees[mouse_pos][cat_pos][0] = len(graph[mouse_pos])
                degrees[mouse_pos][cat_pos][1] = len(graph[cat_pos]) - graph[cat_pos].count(0)

        states_queue = deque()

        # Initialize the queue with base cases where the game is already decided.
        for i in range(1, len(graph)):
            result[0][i][0] = 1
            result[0][i][1] = 1
            states_queue.append((0, i, 0))
            states_queue.append((0, i, 1))
            result[i][i][0] = 2
            result[i][i][1] = 2
            states_queue.append((i, i, 0))
            states_queue.append((i, i, 1))

        while states_queue:
            mouse_pos, cat_pos, turn = states_queue.popleft()
            curr_result = result[mouse_pos][cat_pos][turn]
            for prev_mouse_pos, prev_cat_pos, prev_turn in self.get_prev_states(mouse_pos, cat_pos, turn):
                if result[prev_mouse_pos][prev_cat_pos][prev_turn] == 0:
                    can_win = ((curr_result == 1) and (prev_turn == 0)) or ((curr_result == 2) and (prev_turn == 1))
                    if can_win:
                        result[prev_mouse_pos][prev_cat_pos][prev_turn] = curr_result
                        states_queue.append((prev_mouse_pos, prev_cat_pos, prev_turn))
                    else:
                        degrees[prev_mouse_pos][prev_cat_pos][prev_turn] -= 1
                        if degrees[prev_mouse_pos][prev_cat_pos][prev_turn] == 0:
                            result[prev_mouse_pos][prev_cat_pos][prev_turn] = curr_result
                            states_queue.append((prev_mouse_pos, prev_cat_pos, prev_turn))
        return result[1][2][0]


    def get_prev_states(self, mouse_pos, cat_pos, turn):
        previous_states = []
        prev_turn = 1 - turn
        if prev_turn == 1:
            for prev_cat_pos in self.graph[cat_pos]:
                if prev_cat_pos != 0:
                    previous_states.append((mouse_pos, prev_cat_pos, prev_turn))
        else:
            for prev_mouse_pos in self.graph[mouse_pos]:
                previous_states.append((prev_mouse_pos, cat_pos, prev_turn))
        return previous_states
