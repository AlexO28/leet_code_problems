# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_dict = {}
        for word in words:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        values = list(set(list(freq_dict.values())))
        val_dict = {}
        for key in freq_dict:
            val = freq_dict[key]
            if val in val_dict:
                val_dict[val].append(key)
            else:
                val_dict[val] = [key]
        values.sort(reverse=True)
        chosen = []
        ind = 0
        while len(chosen) < k:
            keys = val_dict[values[ind]]
            keys.sort()
            chosen.extend(keys)
            ind += 1
        return chosen[:k]
