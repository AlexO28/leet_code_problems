# A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.
# Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.
# Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserves = {}
        for reserve in reservedSeats:
            if reserve[0] in reserves:
                reserves[reserve[0]].append(reserve[1])
            else:
                reserves[reserve[0]] = [reserve[1]]
        res = 2 * (n - len(reserves))
        for j in reserves:
            seats = reserves[j]
            found = False
            for i in range(2, 10):
                if i in seats:
                    found = True
                    break
            if not found:
                res += 2
                continue
            found = False
            for i in range(2, 6):
                if i in seats:
                    found = True
            if not found:
                res += 1
                continue
            found = False
            for i in range(4, 8):
                if i in seats:
                    found = True
            if not found:
                res += 1
                continue
            found = False
            for i in range(6, 10):
                if i in seats:
                    found = True
            if not found:
                res += 1
                continue
        return res
