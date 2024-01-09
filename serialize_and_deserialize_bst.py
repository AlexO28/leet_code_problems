# Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.
# The encoded string should be as compact as possible.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        arr = self.serializeRecursively(root, arr)
        arr = [str(elem) for elem in arr]
        return ','.join(arr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        arr = data.split(',')
        node, index = self.deserializeRecursively(arr, 0)
        return node

    def serializeRecursively(self, tree, arr):
        if tree is None:
            arr.append(None)
            return arr
        arr.append(tree.val)
        arr = self.serializeRecursively(tree.left, arr)
        arr = self.serializeRecursively(tree.right, arr)
        return arr

    def deserializeRecursively(self, arr, index):
        if arr[index] == 'None':
            return None, index + 1
        else:
            num = int(arr[index])
            node = TreeNode(num)
            p1_node, p1_index = self.deserializeRecursively(arr, index + 1)
            node.left = p1_node
            p2_node, p2_index = self.deserializeRecursively(arr, p1_index)
            node.right = p2_node
            return node, p2_index
        
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
