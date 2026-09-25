/*
A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:
If a group of k spectators can sit together in a row.
If every member of a group of k spectators can get a seat. They may or may not sit together.
Note that the spectators are very picky. Hence:
They will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.
In case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest number is chosen.
Implement the BookMyShow class:
BookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.
int[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. Returns [] in case it is not possible to allocate seats to the group.
boolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.
*/
public class BookMyShow {
    private int n;
    private int m;
    private SegmentTree tree;

    public BookMyShow(int n, int m) {
        this.n = n;
        this.m = m;
        tree = new SegmentTree(n, m);
    }
    
    public int[] Gather(int k, int maxRow) {
        ++maxRow;
        int i = tree.QueryIdx(1, 1, maxRow, k);
        if (i == 0) {
            return new int[] {};
        }
        long s = tree.QuerySum(1, i, i);
        tree.Modify(1, i, s - k);
        return new int[] {i - 1, (int) (m - s)};
    }
    
    public bool Scatter(int k, int maxRow) {
        ++maxRow;
        if (tree.QuerySum(1, 1, maxRow) < k) {
            return false;
        }
        int i = tree.QueryIdx(1, 1, maxRow, 1);
        for (int j = i; j <= n; ++j) {
            long s = tree.QuerySum(1, j, j);
            if (s >= k) {
                tree.Modify(1, j, s - k);
                return true;
            }
            k -= (int)s;
            tree.Modify(1, j, 0);
        }
        return true;
    }
}

class SegmentTree {
    private Node[] tr;
    private int m;

    public SegmentTree(int n, int m) {
        this.m = m;
        tr = new Node[n << 2];
        for (int i = 0; i < tr.Length; ++i) {
            tr[i] = new Node();
        }
        Build(1, 1, n);
    }

    private void Build(int u, int l, int r) {
        tr[u].l = l;
        tr[u].r = r;
        if (l == r) {
            tr[u].s = m;
            tr[u].mx = m;
            return;
        } else {
            int u2 = u << 1;
            int mid = (l + r) >> 1;
            Build(u2, l, mid);
            Build(u2 | 1, mid + 1, r);
            Pushup(u);
        }
    }

    public void Modify(int u, int x, long v) {
        if (tr[u].l == x && tr[u].r == x) {
            tr[u].s = v;
            tr[u].mx = v;
        } else {
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (x <= mid) {
                Modify(u << 1, x, v);
            } else {
                Modify(u << 1 | 1, x, v);
            }
            Pushup(u);
        }
    }

    public long QuerySum(int u, int l, int r) {
        if (tr[u].l >= l && tr[u].r <= r) {
            return tr[u].s;
        }
        int mid = (tr[u].l + tr[u].r) >> 1;
        long v = 0;
        if (l <= mid) {
            v += QuerySum(u << 1, l, r);
        }
        if (r > mid) {
            v += QuerySum(u << 1 | 1, l, r);
        }
        return v;
    }

    public int QueryIdx(int u, int l, int r, int k) {
        if (tr[u].mx < k) {
            return 0;
        }
        if (tr[u].l == tr[u].r) {
            return tr[u].l;
        }
        int mid = (tr[u].l + tr[u].r) >> 1;
        if (tr[u << 1].mx >= k) {
            return QueryIdx(u << 1, l, r, k);
        }
        if (r > mid) {
            return QueryIdx(u << 1 | 1, l, r, k);
        }
        return 0;
    }

    private void Pushup(int u) {
        tr[u].s = tr[u << 1].s + tr[u << 1 | 1].s;
        tr[u].mx = Math.Max(tr[u << 1].mx, tr[u << 1 | 1].mx);
    }
}

class Node {
    public int l;
    public int r;
    public long mx;
    public long s;
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * BookMyShow obj = new BookMyShow(n, m);
 * int[] param_1 = obj.Gather(k,maxRow);
 * bool param_2 = obj.Scatter(k,maxRow);
 */
