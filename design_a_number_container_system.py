# Design a number container system that can do the following:
# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:
# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
from bisect import insort_left


class NumberContainers:

    def __init__(self):
        self.numbers_by_index = {}
        self.indices_by_number = {}
        

    def change(self, index: int, number: int) -> None:
        if index in self.numbers_by_index:
            num = self.numbers_by_index[index]
            if len(self.indices_by_number[num]) == 1:
                del self.indices_by_number[num]
            else:
                self.indices_by_number[num].remove(index)
        self.numbers_by_index[index] = number
        if number in self.indices_by_number:
            insort_left(self.indices_by_number[number], index)
        else:
            self.indices_by_number[number] = [index]

    def find(self, number: int) -> int:
        if number in self.indices_by_number:
            return self.indices_by_number[number][0]
        else:
            return -1
