# There are n couples sitting in 2n seats arranged in a row and want to hold hands.
# The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).
# Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        num_couples = len(row) // 2
        self.parent = list(range(num_couples))
        for i in range(0, len(row), 2):
            self.parent[self.find_root_couple(row[i] // 2)] = self.find_root_couple(row[i+1] // 2)
        return num_couples - sum(i == self.find_root_couple(i) for i in range(num_couples))

    def find_root_couple(self, couple):
        if self.parent[couple] != couple:
            self.parent[couple] = self.find_root_couple(self.parent[couple])
        return self.parent[couple]
