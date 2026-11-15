/*
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.
You have to perform m independent queries on the tree where in the ith query you do the following:
Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.
Note:
The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
*/
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
function treeQueries(root: TreeNode | null, queries: number[]): number[] {
    const res: number[] = [];
    const levels: Map<number, [number, number][]> = new Map();
    const valToLevel = new Map<number, number>();
    search(root, 0, levels, valToLevel);
    for (const [_, l] of levels) {
        l.sort(([a], [b]) => b - a);
    }
    for (const q of queries) {
        const level: number = valToLevel.get(q)!;
        const maxes: [number, number][] = levels.get(level)!;
        if (maxes.length === 1) {
            res.push(level - 1);
        } else {
            const [val0, max0, max1] = [maxes[0][1], maxes[0][0], maxes[1][0]];
            const max: number = val0 === q ? max1 : max0;
            res.push(max);
        }
    }
    return res;
};


function search(node: TreeNode | null, level: number, levels: Map<number, [number, number][]>, valToLevel: Map<number, number>): number {
    if (!node) {
        return level - 1;
    }
    const max: number = Math.max(search(node.left, level + 1, levels, valToLevel), search(node.right, level + 1, levels, valToLevel));
    if (!levels.has(level)) {
        levels.set(level, []);
    }
    levels.get(level)?.push([max, node.val]);
    valToLevel.set(node.val, level);
    return max;
};
