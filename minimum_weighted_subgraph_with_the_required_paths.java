/*
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.
You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.
Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.
Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.
A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.
*/
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;


class Solution {
    private static final Long INF = Long.MAX_VALUE;

    public long minimumWeight(int n, int[][] edges, int src1, int src2, int dest) {
        List<Pair<Integer, Long>>[] g = new List[n];
        List<Pair<Integer, Long>>[] rg = new List[n];
        for (int i = 0; i < n; ++i) {
            g[i] = new ArrayList<>();
            rg[i] = new ArrayList<>();
        }
        for (int[] e : edges) {
            int f = e[0]; 
            int t = e[1];
            long w = e[2];
            g[f].add(new Pair<>(t, w));
            rg[t].add(new Pair<>(f, w));
        }
        long[] d1 = dijkstra(g, src1);
        long[] d2 = dijkstra(g, src2);
        long[] d3 = dijkstra(rg, dest);
        long ans = -1;
        for (int i = 0; i < n; ++i) {
            if (d1[i] == INF || d2[i] == INF || d3[i] == INF) {
                continue;
            }
            long t = d1[i] + d2[i] + d3[i];
            if (ans == -1 || ans > t) {
                ans = t;
            }
        }
        return ans;
    }

    private long[] dijkstra(List<Pair<Integer, Long>>[] g, int u) {
        long[] dist = new long[g.length];
        Arrays.fill(dist, INF);
        dist[u] = 0;
        PriorityQueue<Pair<Long, Integer>> q
            = new PriorityQueue<>(Comparator.comparingLong(Pair::getKey));
        q.offer(new Pair<>(0L, u));
        while (!q.isEmpty()) {
            Pair<Long, Integer> p = q.poll();
            long d = p.getKey();
            u = p.getValue();
            if (d > dist[u]) {
                continue;
            }
            for (Pair<Integer, Long> e : g[u]) {
                int v = e.getKey();
                long w = e.getValue();
                long temp = dist[u] + w;
                if (dist[v] > temp) {
                    dist[v] = temp;
                    q.offer(new Pair<>(dist[v], v));
                }
            }
        }
        return dist;
    }
}

class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
}
