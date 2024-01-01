# A password is considered strong if the below conditions are all met:
# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
# Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.
# In one step, you can:
# Insert one character to password,
# Delete one character from password, or
# Replace one character of password with another character.
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        char_types = self.count_char_types(password)
        length = len(password)
        if length < 6:
            return max(6 - length, char_types)
        replaces = 0
        oneSeq = 0
        twoSeq = 0
        i = 2
        while i < length:
            if (password[i] == password[i-1]) & (password[i-1] == password[i-2]):
                consecutive = 2
                while i < length: 
                    if password[i] == password[i-1]:
                        consecutive += 1
                        i += 1
                    else:
                        break
                replaces += consecutive // 3
                if consecutive % 3 == 0:
                    oneSeq += 1
                elif consecutive % 3 == 1:
                    twoSeq += 1
            else:
                i += 1
        if length <= 20:
            return max(replaces, char_types)
        deletes = len(password) - 20
        replaces -= min(oneSeq, deletes)
        replaces -= min(max(deletes - oneSeq, 0), twoSeq * 2) // 2
        replaces -= max(deletes - oneSeq - twoSeq * 2, 0) // 3
        return deletes + max(replaces, char_types)

    def count_char_types(self, s):
        has_lower = 1
        has_upper = 1
        has_digit = 1
        for elem in s:
            if elem.islower():
                has_lower = 0
            elif elem.isupper():
                has_upper = 0
            elif elem.isdigit():
                has_digit = 0
        return has_lower + has_upper + has_digit
