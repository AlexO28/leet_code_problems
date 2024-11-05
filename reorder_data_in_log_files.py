# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
# There are two types of logs:
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            words = log.split(" ")
            if ("0" in words[1]) or ("1" in words[1]) or ("2" in words[1]) or ("3" in words[1]) or ("4" in words[1]) or ("5" in words[1]) or ("6" in words[1]) or ("7" in words[1]) or ("8" in words[1]) or ("9" in words[1]):
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def fun(x):
            words = x.split(" ")
            return " ".join(words[1:]), words[0]

        letter_logs = sorted(letter_logs, key = lambda x: fun(x))
        letter_logs.extend(digit_logs)
        return letter_logs
