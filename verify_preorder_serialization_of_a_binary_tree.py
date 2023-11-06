# One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.
# Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        if len(preorder) == 1:
            return preorder[0] == "#"
        if preorder[0] == "#":
            return False
        admissible_number = 2
        for j in range(1, len(preorder)):
            if preorder[j] == "#":
                admissible_number -= 1
            else:
                admissible_number += 1
            if admissible_number < 0:
                return False
            elif (admissible_number == 0) and (j != (len(preorder)-1)):
                return False
        return admissible_number == 0
 
