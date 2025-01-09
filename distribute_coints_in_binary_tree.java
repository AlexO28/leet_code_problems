/*
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int totalMoves;

    public int distributeCoins(TreeNode root) {
        totalMoves = 0;
        postOrderTraversal(root);
        return totalMoves;
    }

    private int postOrderTraversal(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int leftMoves = postOrderTraversal(node.left);
        int rightMoves = postOrderTraversal(node.right);
        totalMoves += Math.abs(leftMoves) + Math.abs(rightMoves);
        return leftMoves + rightMoves + node.val - 1;
    }
}
