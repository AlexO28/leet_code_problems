# You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.
# For each move, you could choose any m (1 <= m <= n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.
# Given an integer array machines representing the number of dresses in each washing machine from left to right on the line, return the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        k, mod = divmod(sum(machines), len(machines))
        if mod > 0:
            return -1
        res = 0
        s = 0
        for machine in machines:
            machine -= k
            s += machine
            res = max(res, abs(s), machine)
        return res
