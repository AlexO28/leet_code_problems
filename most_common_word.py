# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_dict = {}
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower()) 
        for word in banned:
            banned_dict[word] = 1
        freq_dict = {}
        for word in paragraph.split(" "):
            if len(word) > 0:
                if word not in banned_dict:
                    if word in freq_dict:
                        freq_dict[word] += 1
                    else:
                        freq_dict[word] = 1
        return max(freq_dict, key=freq_dict.get)
