# Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.
# Implement the MagicDictionary class:
# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
class MagicDictionary:

    def __init__(self):
        pass
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.strings = dictionary
        

    def search(self, searchWord: str) -> bool:
        for string in self.strings:
            if len(string) == len(searchWord):
                num_errors = 0
                for j in range(len(searchWord)):
                    if searchWord[j] != string[j]:
                        num_errors += 1
                        if num_errors == 2:
                            break
                if num_errors == 1:
                    return True 
        return False
