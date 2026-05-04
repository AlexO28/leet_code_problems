# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.
# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        res_dict = {}
        for word in words:
            res_dict[int(word[-1])] = word[:(-1)]
        nums = list(res_dict.keys())
        nums.sort()
        res = []
        for num in nums:
            res.append(res_dict[num])
        return " ".join(res)
