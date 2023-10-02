# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        arr = self.serializeRecursively(root, arr)
        arr = [str(elem) for elem in arr]
        return ','.join(arr)


    def serializeRecursively(self, tree, arr):
        if tree is None:
            arr.append(None)
            return arr
        arr.append(tree.val)
        arr = self.serializeRecursively(tree.left, arr)
        arr = self.serializeRecursively(tree.right, arr)
        return arr
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')
        node, index = self.deserializeRecursively(arr, 0)
        return node


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

