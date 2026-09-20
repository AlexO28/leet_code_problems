# You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].
# A message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.
# Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.
# Note:
# Uppercase letters come before lowercase letters in lexicographical order.
# "Alice" and "alice" are distinct.
class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        senders_info = {}
        for j in range(len(senders)):
            number_of_words = len([elem for elem in messages[j] if elem == ' ']) + 1
            if senders[j] in senders_info:
                senders_info[senders[j]] += number_of_words
            else:
                senders_info[senders[j]] = number_of_words
        max_val = -1
        sender = ""
        for candidate in senders_info:
            if senders_info[candidate] > max_val:
                max_val = senders_info[candidate]
                sender = candidate
            elif senders_info[candidate] == max_val:
                if sender < candidate:
                    sender = candidate
        return sender
