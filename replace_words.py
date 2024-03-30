# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
# Return the sentence after the replacement.
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        res = []
        for word in words:
            found = []
            for key in dictionary:
                if len(word) >= len(key):
                    if word[:len(key)] == key:
                        found.append(key)
            if len(found) == 0:
                res.append(word)
            else:
                found = sorted(found, key=len)
                res.append(found[0])    
        return " ".join(res)
