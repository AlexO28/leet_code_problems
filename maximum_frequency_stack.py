# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
# Implement the FreqStack class:
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
class FreqStack:

    def __init__(self):
        self.freq_counter = {}
        self.freq_dict = {}
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        if val in self.freq_counter:
            self.freq_counter[val] += 1
        else:
            self.freq_counter[val] = 1
        frequency = self.freq_counter[val]
        if frequency in self.freq_dict:
            self.freq_dict[frequency].append(val)
        else:
            self.freq_dict[frequency] = [val]
        self.max_freq = max(self.max_freq, frequency)

    def pop(self) -> int:
        value = self.freq_dict[self.max_freq].pop()
        if self.freq_counter[value] == 1:
            del self.freq_counter[value]
        else:
            self.freq_counter[value] -= 1
        if not self.freq_dict[self.max_freq]:
            self.max_freq -= 1
        return value
