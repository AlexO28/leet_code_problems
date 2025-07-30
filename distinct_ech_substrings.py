# Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        base = 131
        self.mod = 10**9 + 7
        self.prefix_hashes = [0] * (len(text) + 1)
        self.pow_base = [1] * (len(text) + 1)
        for i, character in enumerate(text):
            char_code = ord(character) - ord("a") + 1
            self.prefix_hashes[i + 1] = (
                self.prefix_hashes[i] * base + char_code
            ) % self.mod
            self.pow_base[i + 1] = (self.pow_base[i] * base) % self.mod
        seen_echo_hashes = set()
        for i in range(len(text) - 1):
            for j in range(i + 1, len(text), 2):
                middle = (i + j) // 2
                hash_first_half = self.get_hash(i + 1, middle + 1)
                hash_second_half = self.get_hash(middle + 2, j + 1)
                if hash_first_half == hash_second_half:
                    seen_echo_hashes.add(hash_first_half)
        return len(seen_echo_hashes)

    def get_hash(self, l, r):
        return (
            self.prefix_hashes[r] - self.prefix_hashes[l - 1] * self.pow_base[r - l + 1]
        ) % self.mod
