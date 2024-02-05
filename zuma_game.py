# You are playing a variation of the game Zuma.
# In this variation of Zuma, there is a single row of colored balls on a board, where each ball can be colored red 'R', yellow 'Y', blue 'B', green 'G', or white 'W'. You also have several colored balls in your hand.
# Your goal is to clear all of the balls from the board. On each turn:
# Pick any ball from your hand and insert it in between two balls in the row or on either end of the row.
# If there is a group of three or more consecutive balls of the same color, remove the group of balls from the board.
# If this removal causes more groups of three or more of the same color to form, then continue removing each group until there are none left.
# If there are no more balls on the board, then you win the game.
# Repeat this process until you either win or do not have any more balls in your hand.
# Given a string board, representing the row of balls on the board, and a string hand, representing the balls in your hand, return the minimum number of balls you have to insert to clear all the balls from the board. If you cannot clear all the balls from the board using the balls in your hand, return -1.
import collections

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand = "".join(sorted(hand))
        q = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])
        while q:
            curr_board, curr_hand, step = q.popleft()
            for i in range(len(curr_board)+1):
                for j in range(len(curr_hand)):
                    if j > 0 and curr_hand[j] == curr_hand[j-1]:
                        continue                    
                    if i > 0 and curr_board[i-1] == curr_hand[j]:
                        continue                   
                    pick = False
                    if i < len(curr_board) and curr_board[i] == curr_hand[j]:
                        pick = True
                    if 0<i<len(curr_board) and curr_board[i-1] == curr_board[i] and curr_board[i] != curr_hand[j]:
                        pick = True                    
                    if pick:
                        new_board = self.remove_same(curr_board[:i] + curr_hand[j] + curr_board[i:], i)
                        new_hand = curr_hand[:j] + curr_hand[j+1:]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            q.append((new_board, new_hand, step+1))
                            visited.add((new_board, new_hand))
        return -1
    
    def remove_same(self, s, i):
        if i < 0:
            return s
        left = i
        right = i
        while left > 0 and s[left-1] == s[i]:
            left -= 1
        while right+1 < len(s) and s[right+1] == s[i]:
            right += 1
        length = right - left + 1
        if length >= 3:
            new_s = s[:left] + s[right+1:]
            return self.remove_same(new_s, left-1)
        else:
            return s
