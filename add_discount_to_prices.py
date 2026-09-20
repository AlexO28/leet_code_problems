# A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.
# You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.
# Return a string representing the modified sentence.
# Note that all prices will contain at most 10 digits.
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        new_words = []
        for word in words:
            if "e" in word:
                new_words.append(word)
            elif word[0] == "$":
                try:
                    price = round(float(word[1:]) * (100 - discount) / 100, 2)
                    price = str(price)
                    main_part, remainder = price.split(".")
                    if len(remainder) == 1:
                        remainder += "0"
                    new_words.append("$" + main_part + "." + remainder)
                except:
                    new_words.append(word)
            else:
                new_words.append(word)
        return " ".join(new_words)
