# You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
# A 0-indexed string num of length n + 1 is created using the following conditions:
# num consists of the digits '1' to '9', where each digit is used at most once.
# If pattern[i] == 'I', then num[i] < num[i + 1].
# If pattern[i] == 'D', then num[i] > num[i + 1].
# Return the lexicographically smallest possible string num that meets the conditions.
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.visited = [False] * 10
        self.current_number = []
        self.smallest = None
        self.search(0, pattern)
        return self.smallest


    def search(self, position, pattern):
        if self.smallest:
            return
        if position == len(pattern) + 1:
            self.smallest = ''.join(self.current_number)
            return
        for digit in range(1, 10):
            if not self.visited[digit]:
                if position and pattern[position - 1] == 'I' and int(self.current_number[-1]) >= digit:
                    continue
                if position and pattern[position - 1] == 'D' and int(self.current_number[-1]) <= digit:
                    continue
                self.visited[digit] = True
                self.current_number.append(str(digit))
                self.search(position + 1, pattern)
                self.visited[digit] = False
                self.current_number.pop()
