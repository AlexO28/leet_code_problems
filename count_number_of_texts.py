# Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.
# In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.
# For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
# Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
# However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.
# For example, when Alice sent the message "bob", Bob received the string "2266622".
# Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.
# Since the answer may be very large, return it modulo 109 + 7.
from functools import cache


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        groups = []
        groups_9 = []
        prev_symb = pressedKeys[0]
        group_size = 0
        for elem in pressedKeys:
            if elem == prev_symb:
                group_size += 1
            else:
                if prev_symb in "79":
                    groups_9.append(group_size)
                else:
                    groups.append(group_size)
                group_size = 1
                prev_symb = elem
        if prev_symb in "79":
            groups_9.append(group_size)
        else:
            groups.append(group_size)
        self.MOD = 1000000007
        res = 1
        for elem in groups:
            res = (res * self.calculate_standard_group(elem)) % self.MOD
        for elem in groups_9:
            res = (res * self.calculate_group_of_nines(elem)) % self.MOD
        return res

    @cache
    def calculate_standard_group(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            return (
                self.calculate_standard_group(n - 1)
                + self.calculate_standard_group(n - 2)
                + self.calculate_standard_group(n - 3)
            ) % self.MOD

    @cache
    def calculate_group_of_nines(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        elif n == 4:
            return 8
        else:
            return (
                self.calculate_group_of_nines(n - 1)
                + self.calculate_group_of_nines(n - 2)
                + self.calculate_group_of_nines(n - 3)
                + self.calculate_group_of_nines(n - 4)
            ) % self.MOD
