# You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
# Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
# Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        temp = Node(None, None, None, None)
        self.flatten_list(temp, head)
        temp.next.prev = None
        return temp.next

    def flatten_list(self, prev_node, current_node):
        if current_node is None:
            return prev_node
        current_node.prev = prev_node
        prev_node.next = current_node
        next_node = current_node.next
        tail = self.flatten_list(current_node, current_node.child)
        current_node.child = None
        return self.flatten_list(tail, next_node)
