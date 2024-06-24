# There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].
# The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.
# Return any string of minimum length that will unlock the safe at some point of entering it.
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join([str(i) for i in range(k)])
        if k == 1:
            return "0"*n
        self.passwordSize = k ** n
        path = "0"*n
        self.visited = set()
        self.visited.add(path)
        self.k = k
        self.n = n
        return self.search(path)
        
    def search(self, path):
        if len(self.visited) == self.passwordSize:
            return path
        for c in range(self.k):
            c = str(c)
            node = path[-self.n+1:] + c
            if node not in self.visited:
                self.visited.add(node)
                res = self.search(path + c)
                if res:
                    return res
                self.visited.remove(node)
