# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        character_stack = []
        for character in s:
            if character_stack and character_stack[-1][0] == character:
                character_stack[-1][1] += 1
                if character_stack[-1][1] == k:
                    character_stack.pop()
            else:
                character_stack.append([character, 1])
        result = "".join(character * count for character, count in character_stack)
        return result
