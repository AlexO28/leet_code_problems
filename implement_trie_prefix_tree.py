class Trie:

    def __init__(self):
        self.strings = []

    def insert(self, word: str) -> None:
        if word not in self.strings:
            self.strings.append(word)

    def search(self, word: str) -> bool:
        return word in self.strings

    def startsWith(self, prefix: str) -> bool:
        if len(self.strings) == 0:
            return False
        for string in self.strings:
            if len(string) >= len(prefix):
                if string[:(len(prefix))] == prefix:
                    return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
