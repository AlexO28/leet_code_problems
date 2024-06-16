# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".
# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licenseDict = {}
        for elem in licensePlate:
            if elem.isalpha():
                elem = elem.lower()
                if elem in licenseDict:
                    licenseDict[elem] += 1
                else:
                    licenseDict[elem] = 1
        words = sorted(words, key=len)
        for word in words:
            word_freq = {}
            for symb in word:
                if symb in word_freq:
                    word_freq[symb] += 1
                else:
                    word_freq[symb] = 1
            terminate = True
            for key in licenseDict.keys():
                if key not in word_freq:
                    terminate = False
                    break
                else:
                    if word_freq[key] < licenseDict[key]:
                        terminate = False
                        break
            if terminate:
                return word
