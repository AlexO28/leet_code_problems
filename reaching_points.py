# Given four integers sx, sy, tx, and ty, return true if it is possible to convert the point (sx, sy) to the point (tx, ty) through some operations, or false otherwise.
# The allowed operation on some point (x, y) is to convert it to either (x, x + y) or (x + y, y).
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while (tx > sx) and (ty > sy) and (tx != ty):
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if (tx == sx) and (ty == sy):
            return True
        elif (tx == sx):
            return (ty > sy) and ((ty - sy) % tx == 0)
        elif (ty == sy):
            return (tx > sx) and ((tx - sx) % ty == 0)
        else:
            return False
