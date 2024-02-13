# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.
# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq_dict, summas = self.findFrequencies(root)
        max_freq = max(list(freq_dict.values()))
        return [elem for elem in freq_dict.keys() if freq_dict[elem] == max_freq]

    def findFrequencies(self, tree):
        if (tree.left is None) and (tree.right is None):
            return {tree.val: 1}, tree.val
        elif (tree.left is None) and (tree.right is not None):
            freq_dict, summas = self.findFrequencies(tree.right)
            summa = tree.val + summas
            if summa in freq_dict:
                freq_dict[summa] += 1
            else:
                freq_dict[summa] = 1
            return freq_dict, summa
        elif (tree.right is None) and (tree.left is not None):
            freq_dict, summas = self.findFrequencies(tree.left)
            summa = tree.val + summas
            if summa in freq_dict:
                freq_dict[summa] += 1
            else:
                freq_dict[summa] = 1
            return freq_dict, summa
        else:
            freq_dict = {}
            freq_dict_left, summas_left = self.findFrequencies(tree.left)
            freq_dict_right, summas_right = self.findFrequencies(tree.right)
            summa = tree.val + summas_left + summas_right
            for val in freq_dict_left.keys():
                if val in freq_dict:
                    freq_dict[val] += freq_dict_left[val]
                else:
                    freq_dict[val] = freq_dict_left[val]
            for val in freq_dict_right.keys():
                if val in freq_dict:
                    freq_dict[val] += freq_dict_right[val]
                else:
                    freq_dict[val] = freq_dict_right[val]
            if summa in freq_dict:
                freq_dict[summa] += 1
            else:
                freq_dict[summa] = 1
            return freq_dict, summa
