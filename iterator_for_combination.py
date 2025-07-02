# Design the CombinationIterator class:
# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.current_mask = (1 << len(characters)) - 1
        self.combination_size = combinationLength
        self.characters_reversed = characters[::-1]

    def next(self) -> str:
        while (self.current_mask >= 0) and (
            bin(self.current_mask).count("1") != self.combination_size
        ):
            self.current_mask -= 1
        combination = []
        for i in range(len(self.characters_reversed)):
            if (self.current_mask >> i) & 1:
                combination.append(self.characters_reversed[i])
        self.current_mask -= 1
        return "".join(combination[::-1])

    def hasNext(self) -> bool:
        while (self.current_mask >= 0) and (
            bin(self.current_mask).count("1") != self.combination_size
        ):
            self.current_mask -= 1
        return self.current_mask >= 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
