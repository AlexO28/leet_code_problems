# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
class Solution:
    def compress(self, chars: List[str]) -> int:
        symb_prev = ""
        counter = 0
        res = []
        for symb in chars:
            if symb == symb_prev:
                counter += 1
            else:
                if symb_prev != "":
                    res.append(symb_prev)
                    if counter > 1:
                        counter = list(str(counter))
                        res.extend(counter)
                counter = 1
                symb_prev = symb
        res.append(symb_prev)
        if counter > 1:
            counter = list(str(counter))
            res.extend(counter)
        for j in range(len(res)):
            chars[j] = res[j]
        chars = chars[:len(res)]
        return len(res)
  
