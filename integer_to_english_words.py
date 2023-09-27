# Convert a non-negative integer num to its English words representation.


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        num = str(num)
        if len(num) < 10:
            num = "0"*(10-len(num)) + num
        phrase = []
        if num[0] != "0":
            phrase.append(self.numToWord(num[0]))
            phrase.append("Billion")
        if num[1] != "0":
            phrase.append(self.numToWord(num[1]))
            phrase.append("Hundred")
        if num[2] != "0":
            phrase.append(self.numToWord2(num[2]))
        if num[3] != "0":
            phrase = self.modify_phrase(phrase, self.numToWord(num[3]))
        if (num[1] != "0") or (num[2] != "0") or (num[3] != "0"):
            phrase.append("Million")
        if num[4] != "0":
            phrase.append(self.numToWord(num[4]))
            phrase.append("Hundred")
        if num[5] != "0":
            phrase.append(self.numToWord2(num[5]))
        if num[6] != "0":
            phrase = self.modify_phrase(phrase, self.numToWord(num[6]))
        if (num[4] != "0") or (num[5] != "0") or (num[6] != "0"):
            phrase.append("Thousand")
        if num[7] != "0":
            phrase.append(self.numToWord(num[7]))
            phrase.append("Hundred")
        if num[8] != "0":
            phrase.append(self.numToWord2(num[8]))
        if num[9] != "0":
            phrase = self.modify_phrase(phrase, self.numToWord(num[9]))
        return ' '.join(phrase)

    def numToWord(self, num):
        if num == "1":
            return "One"
        if num == "2":
            return "Two"
        if num == "3":
            return "Three"
        if num == "4":
            return "Four"
        if num == "5":
            return "Five"
        if num == "6":
            return "Six"
        if num == "7":
            return "Seven"
        if num == "8":
            return "Eight"
        if num == "9":
            return "Nine"
        return ""

    def numToWord2(self, num):
        if num == "1":
            return "Ten"
        if num == "2":
            return "Twenty"
        if num == "3":
            return "Thirty"
        if num == "4":
            return "Forty"
        if num == "5":
            return "Fifty"
        if num == "6":
            return "Sixty"
        if num == "7":
            return "Seventy"
        if num == "8":
            return "Eighty"
        if num == "9":
            return "Ninety"
        return ""

    def modify_phrase(self, phrase, word):
        if len(phrase) > 0:
            if (phrase[-1] == "Ten") and (word == "One"):
                phrase[-1] = "Eleven"
            elif (phrase[-1] == "Ten") and (word == "Two"):
                phrase[-1] = "Twelve"
            elif (phrase[-1] == "Ten") and (word == "Three"):
                phrase[-1] = "Thirteen"
            elif (phrase[-1] == "Ten") and (word == "Four"):
                phrase[-1] = "Fourteen"
            elif (phrase[-1] == "Ten") and (word == "Five"):
                phrase[-1] = "Fifteen"
            elif (phrase[-1] == "Ten") and (word == "Six"):
                phrase[-1] = "Sixteen"
            elif (phrase[-1] == "Ten") and (word == "Seven"):
                phrase[-1] = "Seventeen"
            elif (phrase[-1] == "Ten") and (word == "Eight"):
                phrase[-1] = "Eighteen"
            elif (phrase[-1] == "Ten") and (word == "Nine"):
                phrase[-1] = "Nineteen"
            else:
                phrase.append(word)
        else:
            phrase.append(word)
        return phrase
