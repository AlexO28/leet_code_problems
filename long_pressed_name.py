# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        freqs_name, letters_name = self.form_frequencies(name)
        freqs_typed, letters_typed = self.form_frequencies(typed)
        if len(letters_name) != len(letters_typed):
            return False
        if letters_name != letters_typed:
            return False
        for j in range(len(freqs_name)):
            if freqs_name[j] > freqs_typed[j]:
                return False
        return True
        
    def form_frequencies(self, phrase):
        prev_symb = phrase[0]
        freqs = []
        letters = []
        count = 0
        for j in range(len(phrase)):
            if phrase[j] != prev_symb:
                freqs.append(count)
                letters.append(prev_symb)
                prev_symb = phrase[j]
                count = 1
            else:
                count += 1
        freqs.append(count)
        letters.append(prev_symb)
        return freqs, letters
