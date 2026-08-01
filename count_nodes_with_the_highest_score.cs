/*
There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. Since node 0 is the root, parents[0] == -1.
Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.
Return the number of nodes that have the highest score.
*/
class Solution {
    public: int countHighestScoreNodes(vector < int > & parents) {
        vector < vector < int >> g(parents.size());
        for (int i = 1; i < parents.size(); ++i) {
            g[parents[i]].push_back(i);
        }
        ans = 0;
        mx = 0;
        search(0, -1, g);
        return ans;
    }
    private: int ans;
    long long mx;
    int search(int i, int fa,
        const vector < vector < int >> & g) {
        long long score = 1;
        int cnt = 1;
        for (int j: g[i]) {
            if (j != fa) {
                int t = search(j, i, g);
                cnt += t;
                score *= t;
            }
        }
        if (g.size() - cnt) {
            score *= g.size() - cnt;
        }
        if (mx < score) {
            mx = score;
            ans = 1;
        } else if (mx == score) {
            ++ans;
        }
        return cnt;
    }
};
