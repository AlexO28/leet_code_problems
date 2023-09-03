class WordDictionary:

    def __init__(self):
        self.words = []
        self.called_words = []
        self.absent_words = []
        
    def addWord(self, word: str) -> None:
        if word not in self.words:
            self.words.append(word)
            try:
                self.absent_words.remove(word)
            except:
                0
        
    def search(self, word: str) -> bool:
        if word in self.called_words:
            return True
        if word in self.absent_words:
            return False
        for aword in self.words:
            if len(aword) == len(word):
                terminate = False
                for j in range(len(word)):
                    if (word[j] != "."):
                        if (word[j] != aword[j]):
                            terminate = True
                            break
                if not terminate:
                    self.called_words.append(word)
                    return True
        if '.' not in word:
            self.absent_words.append(word)
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
